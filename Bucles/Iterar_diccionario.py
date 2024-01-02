diccionario = {
  "nombre": "Pepe",
  "apellido": "Sech",
  "years": 248,
  "dinero": 0
}

#Recorriendo el diccionario para obtener las claves
for key in diccionario:
  print(key)

#Recorriendo el diccionario para obtener las claves y el valor
for datos in diccionario.item():
  key = datos[0]
  valor = datos[1]
  print(f'{key} es: {valor}')