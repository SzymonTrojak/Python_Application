from logger_config import logger

class Employee:
    __max_id = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = Employee.__max_id
        self.salary = salary
        Employee.__max_id += 1
        self.logger = logger
        self.logger.info(f"Created new Employee: {self}")

    def display_info(self):
        self.logger.debug(f"Displaying information for Employee {self.employee_id}.")
        return f"Employee ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary} zł"

    def update_salary(self, new_salary):
        self.salary = new_salary
        self.logger.info(f"Updated salary for Employee {self.employee_id}: {self.salary} zł")

if __name__ == "__main__":
    employee1 = Employee("Jan", "Nowak", 5000.00)
    print(employee1.display_info())
    employee1.update_salary(5500.00)
