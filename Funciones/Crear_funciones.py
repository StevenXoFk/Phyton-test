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

#creando una funcion que nos retorne multiples valores 
def crear_contraseña_random(num):
  chars = "abcdefghij"
  num_entero = str(num)
  num = int(num_entero[0])
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
  return contraseña,num
  
#desempaquetando la funcion
password,primer_num = crear_contraseña_random(983)

# imprimiendo los resultados obtenidos y los dstos utilizados
print(password)
print(primer_num)