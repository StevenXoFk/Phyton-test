def obtener_compañeros(cantidad):
  compañeros = []
  for i in range(cantidad_compañeros):
    nombre = input("Cual es tu nombre: ")
    edad = int(input("Cual es tu edad: "))
    compañero = (nombre,edad)
    compañeros.append(compañero)