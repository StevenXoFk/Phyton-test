# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# duración crudo
crudo_promedio = 5
crudos_dalto = 3.5

# Diferencia de duraxion (ejercicio A)
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
#Ejercicio A
print(f'El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de dalto dura un {diferencia_con_promedio}% menos que el mas promedio')

#Ejercicio b
 # calculando el procentaje vacio
vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
vacio_dalto = 100 - dalto_curso * 1000 // crudos_dalto / 10
 
 
print(f'este curso elimina un {vacio_promedio}% de tiempo vacio del promedio')
print(f'este curso elimina un {vacio_dalto}% de tiempo vacio del promedio')

# Mostrando la diferencia de ver 10 horas
print(f'entonces equivaldria un {otros_cursos_promedio * 100 // crudos_dalto / 10}')