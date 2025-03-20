import csv


with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\dat\\trcsv\\employees.csv") as file:
    data = csv.reader(file)
    
    next(data)  
   
    departamentos = {}
    
  
    for row in data:
        department_id = row[10]  
        
        
        if department_id not in departamentos:
            departamentos[department_id] = 0
    
        


for department_id, count in departamentos.items():
    print(f"Departamento {department_id}")
        
      

# Mostrar los resultados
for department_id, employees in departamentos.items():
    print(f"Departamento {department_id}")
    