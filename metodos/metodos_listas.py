# Creando una lista con list()
lista = list(["Steven", "Pepe", 10, 1.2])

# Devuelve la cantidad de elementos en la lista
cantidad = len(lista)

# Agrega un elemento a la lista
lista.append("LOOOOOOL")

# Agrega un elemento a la lista en un indice/posición especifica
lista.insert(1, "Didididi")

# Agrega varios elementos a la lista
lista.extend([True, False, 20202, "meme", "pepeepep"])

# Elimina un elemento de la lista por su indice/posición
lista.pop(-1) # -1 para eliminar el ultimo, -2 el ante ultimo y asi sucesivamente 

# Remueve un elemento de la lista por su valor
lista.remove("Steven")

#Elimina todos los elementos de la lista
lista.clear()

print(lista)