import csv

def find_min_max_salary(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        min_salary = float('inf')
        max_salary = float('-inf')
        min_employee = None
        max_employee = None

        for row in reader:
            salary = float(row['SALARY'])
            if salary < min_salary:
                min_salary = salary
                min_employee = row
            if salary > max_salary:
                max_salary = salary
                max_employee = row

        return min_employee, max_employee

min_emp, max_emp = find_min_max_salary('employees.csv')
print(f"Empleado con salario más bajo: {min_emp['FIRST_NAME']} {min_emp['LAST_NAME']} con salario {min_emp['SALARY']}")
print(f"Empleado con salario más alto: {max_emp['FIRST_NAME']} {max_emp['LAST_NAME']} con salario {max_emp['SALARY']}")