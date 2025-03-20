import csv

def group_by_manager():
    with open('employees.csv', mode='r') as file:
        reader = csv.DictReader(file)
        managers = {}
        
        for row in reader:
            manager_id = row['MANAGER_ID']
            if manager_id not in managers:
                managers[manager_id] = []
            managers[manager_id].append(row)
        
        return managers

managers = group_by_manager()
for manager_id, employees in managers.items():
    print(f"Manager {manager_id}: {len(employees)} empleados")