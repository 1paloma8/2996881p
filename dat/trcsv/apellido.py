import csv


with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\dat\\trcsv\\employees.csv") as file:
    data = csv.reader(file)
    
    next(data)  

    empleados = []

    for row in data:
        employee_first_name = row[1]  
        employee_last_name = row[2]  
        
       
        empleados.append({
            "Nombre": employee_first_name,
            "Apellido": employee_last_name
        })
    
   
    empleados.sort(key=lambda x: x["Apellido"])

# Mostrar los resultados
print("Empleados ordenados por apellido:")
for empleado in empleados:
    print(f"{empleado['Apellido']}, {empleado['Nombre']}")