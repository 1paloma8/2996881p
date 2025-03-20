import csv
with open("C:\\Users\\FORMACION.SIBAPRSESFSD058\\Documents\\prada\\dat\\trcsv\\employees.csv") as file :
    data= csv.reader(file)
    print(type(data))
    for x in data:
        print(x[6])
    

