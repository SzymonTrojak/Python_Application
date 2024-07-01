from logger_config import logger

class Ambulance:
    __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment']
    __max_id = 0

    def __init__(self, vehicle_type, status, location, medical_equipment):
        self.logger = logger
        self.vehicle_type = vehicle_type
        self.status = status
        self.set_location(location)  # użyj metody set_location dla walidacji
        self.medical_equipment = medical_equipment  # List of medical equipment names
        self.id = Ambulance.__max_id
        Ambulance.__max_id += 1
        self.logger.info(f"Ambulance created: {self}")

    def set_location(self, location):
        if not (-90 <= location[0] <= 90 and -180 <= location[1] <= 180):
            self.logger.error(f"Invalid location: {location}")
            raise ValueError(f"Invalid location: {location}")
        self.location = location

    def update_location(self, new_location):
        self.set_location(new_location)
        self.logger.info(f"Ambulance ID {self.id} location updated to {new_location}")

    def __eq__(self, other):
        if not isinstance(other, Ambulance):
            return NotImplemented
        is_equal = self.id == other.id and self.vehicle_type == other.vehicle_type
        self.logger.debug(f"Comparing Ambulance ID {self.id} with Ambulance ID {other.id}: {'equal' if is_equal else 'not equal'}")
        return is_equal

    def __str__(self):
        return (f"Ambulance ID: {self.id}, Type: {self.vehicle_type}, "
                f"Status: {self.status}, Location: {self.location}, "
                f"Equipment: {', '.join(self.medical_equipment)}")

    @staticmethod
    def validate_id(ambulance_id):
        is_valid = isinstance(ambulance_id, int) and ambulance_id > 0
        logger.info(f"Validating Ambulance ID {ambulance_id}: {'valid' if is_valid else 'invalid'}")
        return is_valid

    @classmethod
    def get_instances_count(cls):
        logger.info(f"Getting instances count: {cls.__max_id}")
        return f"Number of working ambulances: {cls.__max_id}"

if __name__ == "__main__":
    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())
