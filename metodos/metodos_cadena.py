cadena1 = "holawe"
cadena2 = "holaaaaaa2"
cadena3 = "hola,pe,po,pi,pu,pa,pe"

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

# Si es alfanumerico de devuelve true y si no false (O sea si el str contiene numeros o la variable contiene numeros devuelve false y si solo contiene strings sin caracteres especiales, devuelve true
alfanumerico = cadena1.isalpha()

# Busca una cadena en otra cadena, pero esta cuenta cuantas coincidencias hay en esa cadena
contar = cadena2.count("a")

# Contamos cuántos caracteres tiene una cadena
caracteres = len(cadena2)

# Verifica si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza = cadena1.startswith("h")

# Verifica si una cadena termina con otra cadena dada, si es asi devuelve true
termina = cadena1.endswith("e")

# si el valor 1, encuentra jna coincidencia en la cadena original, remplaza el valor 1 por el valor del 2
cadena_nueva = cadena1.replace("we", "wi")

# Separa cadenas con cadenas que le pasemos y las convierte en lista
separar = cadena3.split(",")

print(separar)