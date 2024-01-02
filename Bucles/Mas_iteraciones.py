frutas = ["pera", "manzanas","mango","banana","naranja","granada","uvas"]
texto = "Hola Buenas muy bonita tarde"
numeros = [1,9,10,72]

for fruta in frutas:
  print(fruta)
  
# Haciendo que evite un valor psra que continue con otro con continue
for fruta in frutas:
  print(f'La fruta es {fruta}')
  if fruta == 'mango':
    continue
  
# Haciendo que termine el bucle con un determinado valor con break. (El else no se ejecuta cuando se usa el break en el bucle)

for fruta in frutas:
  print(f'La fruta es {fruta}')
  if fruta == 'banana':
    break
print("Bucle terminado")

# recorrer una cadena de texto
for letra in texto:
  print(letra)
  
# for en una sola linea de codigo (multiplicsndo los numeros)

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)