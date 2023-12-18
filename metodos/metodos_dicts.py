diccionario = {
  "nombre": "Pepe",
  "apellido": "Sech",
  "years": 99
}

# claves = diccionario.keys() # Me dice que items hay en el diccionario

# Obteniendo un elemento con get(), y si no encuentra nada no me lanza una excepción y no se para el programa 
claves = diccionario.get("nombre") 

print(claves)