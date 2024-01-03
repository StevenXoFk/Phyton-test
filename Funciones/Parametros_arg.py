#utilizando el operador como argumento (*args)
def suma(nombre,*numeros):
  return f"{nombre}, la suma de tus numeros es {sum(numeros)}"
resultado = suma("lucas",1,4,2,22,35,5)
print(resultado)