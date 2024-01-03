# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# duración crudo
crudo_promedio = 5
crudos_dalto = 3.5

# Diferencia de duraxion (ejercicio A)
diferencia_con_min = round(100 - dalto_curso / otros_cursos_min * 100)
diferencia_con_max = round(100 - dalto_curso / otros_cursos_max * 100,1)
diferencia_con_promedio = round(100 - dalto_curso / otros_cursos_promedio * 100,1)

#Ejercicio A
print("-----------------")
print(f'El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de dalto dura un {diferencia_con_promedio}% menos que el mas promedio')
print("-----------------")

#Ejercicio b
 # calculando el procentaje vacio
vacio_promedio = round(100 - otros_cursos_promedio / crudo_promedio * 100,1)
vacio_dalto = round(100 - dalto_curso / crudos_dalto * 100,1)
 
print("-----------------")
print(f'este curso elimina un {vacio_promedio}% de tiempo vacio del promedio')
print(f'este curso elimina un {vacio_dalto}% de tiempo vacio del promedio')
print("-----------------")

# Mostrando la diferencia de ver 10 horas
print("-----------------")
print(f'entonces equivaldria un {otros_cursos_promedio * 100 // dalto_curso / 10}')
print(f'entonces equivaldria un {dalto_curso * 100 // otros_cursos_promedio / 10}')
print("-----------------")
