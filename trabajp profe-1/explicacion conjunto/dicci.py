import data 
print (data.personas)


paises = ["USA", "AUSTRALIA", "UK", "CANADA"]

for i, persona in enumerate(personas):
    persona["country"] = paises[i % len(paises)]  
print(personas)

# Ejemplo de cómo iterar sobre el diccionario actualizado
for persona in personas:
    print(f"Persona: {persona['name']}, País: {persona['country']}")
    


