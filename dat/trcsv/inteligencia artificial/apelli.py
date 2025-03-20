import csv

def sort_by_last_name():
    with open('employees.csv', mode='r') as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: row['LAST_NAME'])
        
        return sorted_rows

sorted_employees = sort_by_last_name()
for employee in sorted_employees:
    print(f"{employee['LAST_NAME']}, {employee['FIRST_NAME']}")