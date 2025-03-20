import csv


with open("employees.csv") as file:
    data = csv.reader(file)
    
    
    next(data)
   
    empleados = []
    
   
    for row in data:
       
        nombre = row[1] 
        apellido = row[2]  
        salario = int(row[7])  
   
        empleados.append({
            "Nombre": nombre,
            "Apellido": apellido,
            "Salario": salario
        })
    
    
    empleado_max_salario = max(empleados, key=lambda x: x["Salario"])
    

    empleado_min_salario = min(empleados, key=lambda x: x["Salario"])
    
    print("="*90)
    print("El empleado con el salario más alto es:")
    print(f"Nombre: {empleado_max_salario['Nombre']} {empleado_max_salario['Apellido']}")
    print(f"Salario: {empleado_max_salario['Salario']}")
    
    print("="*90)
    print("\nEl empleado con el salario más bajo es:")
    print(f"Nombre: {empleado_min_salario['Nombre']} {empleado_min_salario['Apellido']}")
    print(f"Salario: {empleado_min_salario['Salario']}")
    print("="*90)