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
  else:
    if edad < 18:
      pronombre = "joven"
    elif edad >= 18:
      pronombre = "señorit@"
  print(f'Hola {pronombre} {nombre} como estas?')

saludar("Pepe","Hombre",19)
saludar("Pepe","Hombre",9)
saludar("Marta","mujer",19)
saludar("Marta","mujer",9)
saludar("Roberto","No binario",19)
saludar("Roberto","no binario",9)