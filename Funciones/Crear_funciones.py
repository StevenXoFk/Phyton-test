# Funcion simple
#def saludar():
#  print("Hola we")
  
# Creando Funcion con parámetros
def saludar(nombre,sexo,edad):
  sexo = sexo.lower()
  edad = int(edad)
  if sexo == "mujer":
    if edad < 18:
      pronombre = "joven"
    elif edad >= 18:
      pronombre = "señorita"
  elif sexo == "hombre":
    if edad < 18:
      pronombre = "joven"
    elif edad >= 18:
      pronombre = "señorito"
  print(f'Hola {pronombre} {nombre} como estas?')

saludar("Pepe","hombre",10)