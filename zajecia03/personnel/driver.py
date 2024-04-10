from .employee import Employee

class Driver(Employee):
    def __init__(self, first_name, last_name, salary, license_number,qualifications):
        Employee.__init__(self, first_name, last_name, salary)
        self.license_number = license_number
        self.qualifications = qualifications

    def display_info(self):
        return f"Driver ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary}, License Number: {self.license_number}, Qualifications: {', '.join(self.qualifications)}"

if __name__ == "__main__":
    driver1 = Driver("Jan", "Kowlaski", 1, 10000.00, "LIC1001", ["BLS"])
    print(driver1.display_info())
