diccionario = {
  "nombre": "Pepe",
  "apellido": "Sech",
  "years": 99
}

# claves = diccionario.keys() # Me dice que items hay en el diccionario
claves = diccionario.get("nombre") # Me devuelve el item que mencioné 

print(claves)