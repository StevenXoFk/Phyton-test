diccionario = {
  "nombre": "Pepe",
  "apellido": "Sech",
  "years": 99
}

# Devuelve un elemento dict_item
claves = diccionario.keys()

# Obteniendo un elemento con get(), y si no encuentra nada no me lanza una excepción y no se para el programa 
valor = diccionario.get("nombre") 

# Elimina todo el diccionario
#diccionario.clear()

print(diccionario)