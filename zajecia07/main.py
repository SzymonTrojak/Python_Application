from fleet.ambulance import Ambulance
from fleet.ambulance_queue import AmbulanceQueue
from fleet.station import Stacje
from operations import *
from personnel import *


def run_application():
    # zdefiniowanie zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance3 = Ambulance("Type B", "available", (51.324454, 18.997652), ["Stretcher", "First Aid Kit"])
    ambulance4 = Ambulance("Type A", "available", (49.376565, 19.154563), ["Defibrillator", "Oxygen tank"])
    ambulance5 = Ambulance("Type C", "available", (51.334565, 20.435457), ["Defibrillator", "Oxygen tank"])

    ambulanceQueue = AmbulanceQueue()
    ambulanceQueue += ambulance1
    ambulanceQueue += ambulance2
    ambulanceQueue += ambulance3
    ambulanceQueue += ambulance4
    ambulanceQueue += ambulance5
    print(ambulanceQueue)

    employee1 = Employee("John", "Deer", 10000.0)
    employee2 = Employee("Jane", "Work", 8000.0)

    driver1 = Driver("Bille", "Jean", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "German", 1500.0, "DL12346", ["ALS"])

    station1 = Stacje((53.095340, 19.920282), ambulance2, driver1, employee1)
    station2 = Stacje((51.055454, 19.926432), ambulance1, driver2, employee2)
    
    if ambulance1 == ambulance2:
        raise ValueError("te same karetki!")
    
    print(Ambulance.get_instances_count())

    print()

    incidentQueue = IncidentQueue()

    # 3 zgłoszenia
    incident1 = Incident("Power outage in sector 4", 2, "27.03.2024 14:45", "Grzegorz Kowalski", (51.045455, 20.122554))
    incident2 = Incident("Fire alarm in building 21", 1, "27.03.2024 09:21", "Matylda Wałczyk", (49.954523, 20.897424))
    incident3 = Incident("Fire alarm in building 41", 1, "27.03.2024 16:21", "Mariusz Kolec", (49.22227, 20.234324))
    incidentQueue += incident1
    incidentQueue += incident2
    incidentQueue += incident3

    # przypisanie karetek
    print(asign_ambulances(ambulanceQueue, incidentQueue))

    incident4 = Incident("Cat hanging on a tree", 3, "06.10.2024 12:45", "Jarek Kret", (18.354245, 21.354345))
    incident5 = Incident("Heart attack", 1, "06.10.2024 10:34", "Krystyna Pawłowicz", (50.343311, 21.454312))
    incidentQueue += incident4
    incidentQueue += incident5

    # przypisanie karetek 2 nowym zgłoszeniom
    print(asign_ambulances(ambulanceQueue, incidentQueue))

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(incidentQueue)

    print()

    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(20000.00)
    print(f"Po podwyżce: {driver1.display_info()}")

    print()

    # zad3 
    print(station1.check_location())
    print(station2.check_location())

if __name__ == "__main__":
    run_application()