# Creando un conjunto con set()
conjunto = set(["dato1", "dato2"])

#metiendo un conjunto en otro conjunto
conjunto1 = frozenset(["dato33", "dato34"])
conjunto2 = {conjunto1, "asd"}

#Teoria de conjuntos
conjunto3 = {1,3,9,5,4}
conjunto4 = {1,3,4}

# Verificar si es un subconjunto
resultado = conjunto4.issubset(conjunto3) #conjunto4 es un subconjunto de conjunto3
resultado2 = conjunto4 <= conjunto3 # Otra forma de Verificar los subconjuntos

# Verificar si es un superconjunto
resultado3 = conjunto3.issuperset(conjunto4) #conjunto3 es un superconjunto de conjunto4
resultado4 = conjunto4 < conjunto3 # Otra forma de Verificar los superconjuntos

#Verifica si hay un numero en común
conjunto5 = {2,9,0,1}
conjunto6 = {3,8,4}

resultado5 = conjunto6.isdisjoint(conjunto5)

print(resultado5)