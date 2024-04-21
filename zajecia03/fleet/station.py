class Stacje:
    __max_id = 0

    def __init__(self, location, ambulance, driver, employee):
        self.id = Stacje.__max_id
        self.location = location # as (northing, easting)
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Stacje.__max_id += 1

    def check_location(self):
        frontText = f"Stacja nr {self.id}: Karetka nr {self.ambulance.id}"
        if (self.location == self.ambulance.location):
            return  frontText + f" jest już na miejscu."
        else:
            return frontText + f" jeszcze nie dotarła."