def obtener_compañeros(cantidad):
  compañeros = []
  for i in range(cantidad):
    nombre = input("Cual es tu nombre: ")
    edad = int(input("Cual es tu edad: "))
    compañero = (nombre,edad)
    compañeros.append(compañero)
  compañeros.sort(key=lambda x:x [1])
  asistente = compañeros[0][0]
  profesor = compañeros[-1][0]
  return asistente,profesor
  
asistente,profesor = obtener_compañeros(3)

print(f'El asistente es: {asistente}')
print(f'El Profesor es: {profesor}')