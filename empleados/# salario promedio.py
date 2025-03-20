# salario promedio 
import json


with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\empleados\\employees1.json", mode='r') as archivo:

    datos = json.load(archivo)
    
 
    total_salario = 0
    
 
    for empleado in datos:
        
        total_salario += int(empleado["SALARY"])

    promedio_salario = total_salario / len(datos)
print(f"El salario promedio es: {promedio_salario}, Nombre: {empleado['FIRST_NAME']} {empleado['LAST_NAME']}")