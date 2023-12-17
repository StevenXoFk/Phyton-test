# Creando una lista con list()
lista = list([73636, 333, 10, 1.2])

# Devuelve la cantidad de elementos en la lista
cantidad = len(lista)

# Agrega un elemento a la lista
lista.append(909)

# Agrega un elemento a la lista en un indice/posición especifica
lista.insert(1, 100)

# Agrega varios elementos a la lista
lista.extend([True, False, 20202, 202022, 2.555])

# Elimina un elemento de la lista por su indice/posición
lista.pop(-1) # -1 para eliminar el ultimo, -2 el ante ultimo y asi sucesivamente 

# Remueve un elemento de la lista por su valor
lista.remove(99)

#Elimina todos los elementos de la lista
# lista.clear()

# Ordena la lista ( si se usa el parametro reverse=True se ordena de mayor a menor)
lista.sort
print(lista)