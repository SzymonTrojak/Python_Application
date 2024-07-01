from datetime import datetime
import math
from logger_config import logger

def asign_ambulances(ambulanceQueue, incidentQueue): 
    def passed_time(given_incident):
        given_time_str = given_incident.time
        given_time = datetime.strptime(given_time_str, "%d.%m.%Y %H:%M")
        current_time = datetime.now()
        time_diff = current_time - given_time
        time_passed_seconds = time_diff.total_seconds()
        return time_passed_seconds

    logger.info("Starting assignment of ambulances.")
    
    available_ambulances = list(filter(lambda ambulance: ambulance.status == "available", ambulanceQueue))
    if len(available_ambulances) > 0:
        feedback = ""

        available_incidents = list(filter(lambda incident: incident.ambulance is None, incidentQueue))
        sorted_incidents = sorted(available_incidents, key=lambda incident: (incident.priorty, passed_time(incident)))
        logger.info(f"Found {len(available_incidents)} available incidents to process.")
    
        for incident in sorted_incidents:
            d_unsorted = {}
            i_location = incident.location
            for ambulance in ambulanceQueue:
                if ambulance.status == "available":
                    a_location = ambulance.location
                    d = math.sqrt((i_location[0] - a_location[0])**2 + (i_location[1] - a_location[1])**2)
                    d_unsorted[ambulance.id] = d

            if not d_unsorted:
                feedback += f"Incydentowi nr {incident.id} nie przydzielono karetki ze względu na brak dostępnych karetek.\n"
                logger.warning(f"No available ambulances for incident ID {incident.id}.")
                break
            else:
                d_sorted = dict(sorted(d_unsorted.items(), key=lambda ambulance_dist: ambulance_dist[1]))
                ambulance_id = next(iter(d_sorted.keys()))
                incident.ambulance = ambulance_id
                for ambulance in ambulanceQueue:
                    if ambulance.id == ambulance_id:
                        ambulance.status = "on mission"
                        break
                feedback += f"Incydentowi nr {incident.id} przydzielono karetkę nr {ambulance_id}.\n"
                logger.info(f"Assigned ambulance ID {ambulance_id} to incident ID {incident.id}.")

    else:
        feedback = "Brak karetek :(\n"
        logger.warning("No available ambulances to assign.")

    logger.info("Finished assignment of ambulances.")
    return feedback
