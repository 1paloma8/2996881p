
from data import personas
print(personas )


    
def obtener_nombres(personas):
        return [persona["name"] for persona in personas]
        
nombres = obtener_nombres(personas)
    
   
print("Nombres de las personas:", nombres)



