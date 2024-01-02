#Creando diccionarios con dict()
diccionario = dict(nombre="Pepe",apellido="sech")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario2 = {frozenset(["dato", "date"]): "lol"}

#Creando diccionarios con fromkeys() con valor none
diccionario3 = dict.fromkeys(["nombre","numero"])

print(diccionario3)