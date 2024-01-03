# Funciones
def volver_registro():
  usuario = input("Registrata tu nombre de usuario: ")
  contraseña = input("Pon tu contraseña")

def registro_fail():
  global usuario, contraseña
  
  while len(usuario) > 20:
    print("Tu nombre de usuario tiene mas de 20 caracteres, intentalo de nuevo")
    usuario, contraseña = volver_registro()
    break
    
  while len(usuario) <= 3 or len(usuario) <= 1:
    print("Tu nombre de usuario tiene menos de 4 caracteres, intentalo de nuevo")
    usuario, contraseña = volver_registro()
    break
  
  while len(contraseña) < 5 or len(contraseña) <= 1:
    print("Tu contraseña es muy corta, intenta de nuevo")
    usuario, contraseña = volver_registro()
    break
def inicio_fail():
  print("Hola we")
  
print("""---------------------------------------------------------------
Bienvenido a PichaWeb, registrate para acceder a
nuestro sistema, recuerda que tu nombre de usuario
debe de tener al menos mas de 4 caracteres y maximo
de 20
---------------------------------------------------------------""")
usuario = input("Registrata tu nombre de usuario maximo 20 caracteres: ")
contraseña = input("Pon tu contraseña")