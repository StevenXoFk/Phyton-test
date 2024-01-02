#Creando diccionarios con dict()
diccionario = dict(nombre="Pepe",apellido="sech")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario2 = {frozenset(["dato", "date"]): "lol"}

#Creando diccionarios con fromkeys() con valor por defecto: none
diccionario3 = dict.fromkeys(["nombre","numero"])

#Creando diccionarios con fromkeys() con 2 parámetros 
diccionario4 = dict.fromkeys(["nombre","numero"], 'lmao')

print(diccionario4)