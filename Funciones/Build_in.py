numero = [1,88,72,98,3]
num = 17.8362
# Encontrar el numero mas alto
num_alto = max(numero)
print(num_alto)

# Encontrar el numero mas bajo
num_bajo = min(numero)
print(num_bajo)

# Redondear a 6 decimales
num_round = round(num,2)
print(num_round)

# Retorna false -> vacio, false, None \ True -> distinto a 0, textos, datos no vacios
resultado_bool = bool(1)
print(resultado_bool)

# Retorna true si todos los datos son verdaderos
resultado_all = all([0,True,"hahsgs"])
print(resultado_all)

# Suma yodos los datos de un iterable (solo números 
resultado_sum = sum(numero)
print(resultado_sum)