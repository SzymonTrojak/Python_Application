from logger_config import logger

class Stacje:
    __max_id = 0

    def __init__(self, location, ambulance, driver, employee):
        self.logger = logger
        self.id = Stacje.__max_id
        self.location = location  # as (northing, easting)
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Stacje.__max_id += 1
        self.logger.info(f"Stacja created: {self}")

    def check_location(self):
        frontText = f"Stacja nr {self.id}: Karetka nr {self.ambulance.id}"
        if self.location == self.ambulance.location:
            message = frontText + " jest już na miejscu."
            self.logger.info(f"Location check for Stacja ID {self.id}: {message}")
            return message
        else:
            message = frontText + " jeszcze nie dotarła."
            self.logger.info(f"Location check for Stacja ID {self.id}: {message}")
            return message

    def __str__(self):
        return (f"Stacja ID: {self.id}, Location: {self.location}, "
                f"Ambulance ID: {self.ambulance.id}, Driver: {self.driver}, "
                f"Employee: {self.employee}")

if __name__ == "__main__":
    from ambulance import Ambulance

    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )

    stacja1 = Stacje(
        location=(50.095340, 19.920282),
        ambulance=ambulance1,
        driver="John Doe",
        employee="Jane Doe"
    )

    print(stacja1.check_location())
    print(stacja1)
