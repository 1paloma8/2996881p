import errno

try:
    s = open("C:\Drivers\storage\R93YC\Drivers", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)
        
        
        
        
        
import errno
 
try:
    stream = open("file", "rt")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("ausente")
    else:
        print("desconocido")