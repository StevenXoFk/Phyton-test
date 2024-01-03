print("""---------------------------------------------------------------
Bienvenido a PichaWeb, registrate para acceder a
nuestro sistema, recuerda que tu nombre de usuario
debe de tener al menos mas de 4 caracteres y maximo
de 20
---------------------------------------------------------------""")
error = False
usuario = input("Registrata tu nombre de usuario maximo 20 caracteres: ")
contraseña = input("Pon tu contraseña")

while error == True:
  print("JSHSHSHSHSHJA")

# Funciones
def volver_registro():
  usuario = input("Registrata tu nombre de usuario: ")
  contraseña = input("Pon tu contraseña")

def registro_fail():
  if len(usuario) > 20:
    print("Tu nombre de usuario tiene menos de 4 caracteres, intentalo de nuevo")
    error = True
    volver_registro()