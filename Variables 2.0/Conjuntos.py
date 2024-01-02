# Creando un conjunto con set()
conjunto = set(["dato1", "dato2"])

#metiendo un conjunto en otro conjunto
conjunto1 = frozenset(["dato33", "dato34"])
conjunto2 = {conjunto1, "asd"}

print(conjunto2)