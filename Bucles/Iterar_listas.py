#===================================================== TODO LO SIGUIENTE TAMBIEN FUNCIONA CON TUPLAS Y                          LISTAS       =====================================================
animales = ["perro","gato","loro","mono","pez"]
numeros = [1,90,62,77,82]
orden = 0

#Recorriendo la lista con for
for animal in animales:
 print (animal)

for numero in numeros:
  resultado = numero*2 
  print(resultado)
  
#Iterando 2 listas del mismo tamaño al mismo tiempo
for animal,numero in zip(animales,numeros):
  print (f'Mostrando lista 1: {animal}')
  print (f'Mostrando lista 2: {numero}')

# Forma no optima de recorrer numeros
for num in range(len(numeros)):
  print(numeros[num])
  
# Forma optima de recorrer una lista con su indice
for num,i in enumerate(numeros):
  valor = i
  indice = num
  print(f'indice: {indice} y valor: {valor}')

# Usando for/else
for numero in numeros:
  print(f'El valor es: {numero}')
else:
  print("El bucle terminó ")