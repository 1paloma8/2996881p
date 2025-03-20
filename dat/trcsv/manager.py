import csv


with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\dat\\trcsv\\employees.csv") as file:
    data = csv.reader(file)
    
    next(data)  
    
    managers = {}
  
    for row in data:
        manager_id = row[9]  
        employee_name = row[1]  
        
        if manager_id not in managers:
            managers[manager_id] = []  
        
        managers[manager_id].append(employee_name)


for manager_id, employees in managers.items():
    print(f"Manager {manager_id}: {employees}")