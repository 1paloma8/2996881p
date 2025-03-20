import csv


with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\dat\\trcsv\\employees.csv") as file:
    data = csv.reader(file)
    
    next(data)  
 
    empleados = []
    
 
    for row in data:
        employee_id = int(row[0])  
        employee_first_name = row[1]  
        employee_last_name = row[2]  
      
        empleados.append({
            "ID": employee_id,
            "Nombre": employee_first_name,
            "Apellido": employee_last_name
        })
    
    empleados.sort(key=lambda x: x["ID"])

print("Empleados ordenados por ID:")
for empleado in empleados:
    print(f"ID: {empleado['ID']}, Nombre: {empleado['Nombre']} {empleado['Apellido']}")