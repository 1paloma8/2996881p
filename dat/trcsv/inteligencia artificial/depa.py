import csv

def group_by_department():
    with open('employees.csv', mode='r') as file:
        reader = csv.DictReader(file)
        departments = {}
        
        for row in reader:
            dept_id = row['DEPARTMENT_ID']
            if dept_id not in departments:
                departments[dept_id] = []
            departments[dept_id].append(row)
        
        return departments

departments = group_by_department()
for dept_id, employees in departments.items():
    print(f"Departamento {dept_id}: {len(employees)} empleados")