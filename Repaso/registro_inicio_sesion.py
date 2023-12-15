print("""---------------------------------------------------------------
Bienvenido a PichaWeb, registrate para acceder a
nuestro sistema, recuerda que tu nombre de usuario
debe de tener al menos mas de 4 caracteres y maximo
de 20
---------------------------------------------------------------""")
usuario = input("Registrata tu nombre de usuario maximo 20 caracteres: ")
contraseña = input("Pon tu contraseña")


def registro_fail():
  usuario = input("Registrata tu nombre de usuario: ")
  contraseña = input("Pon tu contraseña")

if len(usuario) > 20:
  print("Tu nombre de usuario exede los 20 caracteres, vuelve a intentarlo")
  registro_fail()
elif len(usuario) <= 3 or len(usuario) <= 1:
  print("Tu nombre de usuario tiene menos de 4 caracteres, intentalo de nuevo")
  registro_fail()
elif len(contraseña) < 5 or len(contraseña) <= 1:
  print("Tu contraseña es muy corta, intenta de nuevo")
  registro_fail()
else:
  print(f'Bienvenido {usuario}, te has registrado exitosamente, ahora inicia sesion')