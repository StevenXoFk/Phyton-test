# Las Listas si se pueden modificar
lista = ["piña", 22, True]
# Las Tuplas no se pueden modificar
Tupla = ("Piña", 22, True)

# Esto se puede
lista[2] = False

# Esto no
#Tupla[0] = 0

# Creando Conjunto con (set), Estos no se pueden llamar como lo hace las listas o tuplas, ademas no se repiten elementos, ni se puede modificar elementos y son randoms su orden
conjunto = {"Pepe", 22, True, "Sech"}

#print(conjunto[2]) -> No se puede acceder al elemento
#print(conjunto) -> esto si

# Creando Un Diccionario (dict), la estructura es key : value, se separa con coma como el formato json
Diccionario = {
  'nombre' : "Angelo",
  'edad' : 17,
  'altura' : 1.68,
  'graduado' : False
}

print(Diccionario['nombre'])