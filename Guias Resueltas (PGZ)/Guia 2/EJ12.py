# Escriba una función llamada calcular_promedio que reciba una lista de listas donde cada lista contiene las
# notas de un estudiante en tres exámenes. La función debe calcular el promedio de cada alumno y devolver
# una lista de promedios. Utilice las funciones built-in correspondientes.
# Ejemplo1
# notasAlumnos=[[8, 9, 7], [8.5, 7.5, 9], [9, 8, 8.5]]
# resultado = [8.0, 8.33, 8.5]

def calcular_promedio(lista_notas):
    lista_promedio = list(map(lambda notas: sum(notas)/len(notas), lista_notas))
    return lista_promedio

notasAlumnos=[[8, 8, 8], [8.5, 9, 9.5], [7, 10, 4]]

print(calcular_promedio(notasAlumnos)) # [8.0, 8.33, 8.5]