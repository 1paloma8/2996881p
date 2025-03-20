import json 
import csv
with open('employees1.json','r',encoding="utf-8") as eljson:
    data=json.load(eljson)
    print(data)
    
    headers=data[0].keys()
    with open ('archivosjson/empleados.csv','w') as elcsv:
        writer=csv.DictWriter(elcsv,headers)
        writer.writeheader()
        writer.writerows(data)

    