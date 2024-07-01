from personnel.employee import Employee
from logger_config import logger

class Driver(Employee):
    def __init__(self, first_name, last_name, salary, license_number, qualifications):
        super().__init__(first_name, last_name, salary)
        self.license_number = license_number
        self.qualifications = qualifications
        self.logger = logger
        self.logger.info(f"Created new Driver: {self}")

    def display_info(self):
        self.logger.debug(f"Displaying information for Driver {self.employee_id}.")
        return f"Driver ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary}, License Number: {self.license_number}, Qualifications: {', '.join(self.qualifications)}"

if __name__ == "__main__":
    driver1 = Driver("Jan", "Kowalski", 10000.00, "LIC1001", ["BLS"])
    print(driver1.display_info())
