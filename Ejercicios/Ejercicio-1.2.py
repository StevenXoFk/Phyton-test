frase = input("decime una frase y te dire cuanto tardarias: ")
separar_palabra = frase.split(" ")
contar_separado = len(separar_palabra)

print(f'Tardarias {contar_separado/2} segundos diciendo {contar_separado} palabras')
print(f'mientras que dalto lo diria en {contar_separado *100 //2 *1.3 /100} segundos')

if contar_separado >= 120:
  print("Tremendo testamento")