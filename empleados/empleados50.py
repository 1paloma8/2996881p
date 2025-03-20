import json


with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\empleados\\employees1.json", mode='r') as archivo:
 
    datos = json.load(archivo)

    
    empleados_departamento_50 = []

   
    for empleado in datos:
       
        if empleado["DEPARTMENT_ID"] == "50":
        
            empleados_departamento_50.append(empleado)
    
 
    print("lista Empleados del departamento 50:")
    for empleado in empleados_departamento_50:
        print("="*90)
        print(f"Nombre: {empleado['FIRST_NAME']} {empleado['LAST_NAME']}, Departamento ID: {empleado['DEPARTMENT_ID']}")