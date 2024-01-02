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
  res = orden+
  print (f'-{res} Mostrando lista 1: {animal}')
  print (f'-{res} Mostrando lista 2: {numero}')