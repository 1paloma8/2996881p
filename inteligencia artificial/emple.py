import csv

def sort_by_employee_id():
    with open('employees.csv', mode='r') as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: int(row['EMPLOYEE_ID']))
        
        return sorted_rows

sorted_employees = sort_by_employee_id()
for employee in sorted_employees:
    print(f"{employee['EMPLOYEE_ID']}: {employee['FIRST_NAME']} {employee['LAST_NAME']}")