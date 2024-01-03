numeros = [1,2,8,4,6]

#Creando una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(4))

#Lo mismo pero con lambda filter
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))