cadena1 = "HOLAAAA"
cadena2 = "holaaaaaa2"

# Convierte el upper() todo el texto en mayuscula
mayus = cadena2.upper()

# Convierte el lower() todo el texto en minuscula
minus = cadena1.lower()

# Convierte el capitalize() en la primera letra en mayuscula
first_mayus = cadena2.capitalize()

# Busca una cadena en otra cadena, y si no encuentra coincidencia devuelve -1
encontrar = cadena1.find("1")

# Busca una cadena en otra cadena, pero si no encuenta coincidencia devuelve un EXCEPCIÓN 
encontrar_index = cadena2.find("2")

# Si es numerico, devuelve true, y si no false
numerico = cadena2.isnumeric()

# Si es alfanumerico de devuelve true y si no false (O sea si el str contiene numeros o la variable contiene numeros devuelve false y si solo contiene strings devuelve true
alfanumerico = cadena1.isalpha()

print(numerico)