# Realizar una función anónima que tendrá como parámetro de entrada la cantidad de columnas y filas de
# una matriz y la genere según el ejemplo dado.
# Ejemplo 1
# columna=5
# filas=4
# matriz=[[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
# Ejemplo 2
# columna=2
# filas=2
# matriz=[[1, 2], [2, 3]]

generar_matriz = lambda columnas, filas: [[i + j for j in range(1, columnas + 1)] for i in range(1, filas * columnas + 1, columnas)]

matriz = generar_matriz(5,4)
print(matriz)