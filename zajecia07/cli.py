import argparse
from personnel.employee import Employee
from fleet.ambulance import Ambulance
from logger_config import logger

def create_employees(num_employees):
    employees = []
    for i in range(num_employees):
        employee = Employee(f"FirstName{i}", f"LastName{i}", 3000 + i * 100)
        employees.append(employee)
        logger.info(f"Created employee: {employee.first_name} {employee.last_name}")
    return employees

def create_ambulances(num_ambulances):
    ambulances = []
    for i in range(num_ambulances):
        ambulance = Ambulance("TypeA", "Available", (50.0 + i, 20.0 + i), ["MedicalKit"])
        ambulances.append(ambulance)
        logger.info(f"Created ambulance: {ambulance.vehicle_type} with ID {ambulance.id}")
    return ambulances

def check_resources(employees, ambulances, required_ambulances):
    if len(employees) < required_ambulances:
        logger.warning("Not enough employees to operate the required number of ambulances.")
        return False
    if len(ambulances) < required_ambulances:
        logger.warning("Not enough ambulances available.")
        return False
    logger.info("Sufficient resources available.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Resource management for ambulance services.")
    parser.add_argument('--employees', type=int, required=True, help="Number of available employees")
    parser.add_argument('--ambulances', type=int, required=True, help="Number of available ambulances")
    parser.add_argument('--required_ambulances', type=int, required=True, help="Number of required ambulances")

    args = parser.parse_args()

    employees = create_employees(args.employees)
    ambulances = create_ambulances(args.ambulances)
    result = check_resources(employees, ambulances, args.required_ambulances)

    if result:
        print("All resources are sufficient.")
    else:
        print("Insufficient resources.")

if __name__ == "__main__":
    main()
