### EJERCICIO 1###
# Utilizando la información de las ventas de las diferentes zonas de influencia de cada uno los vendedores 
# de la empresa “Si se puede”, usted debe realizar un programa que permita realizar las siguientes tareas:
# 1. Crear un diccionario que permita manejar la información de las ventas en cada zona de cada vendedor.
# 2. Preguntar al usuario si desea modificar alguna información existente en la data, de ser así pedir nombre 
# del vendedor, la zona de influencia y el valor de la venta a modificar.
# 3. Visualizar las ventas totales de la empresa
# 4. Visualizar la zona de mayores ventas.
Diccionario = dict(Nicolas = dict(Norte = 3528, Sur = 2400, Este = 1200, Oeste = 8200), 
                  Daniela= dict(Norte = 3824, Sur=6786, Este = 5598, Oeste = 3612),
                  Maria = dict(Norte = 8008, Sur = 4653, Este = 8425, Oeste = 1000), 
                  Francisco = dict(Norte = 5833, Sur = 6356, Este = 2548, Oeste = 1386))
claves = Diccionario.keys()
print(Diccionario)
pregunta = input('¿Desea modificar alguna alguna informacion existente en la data? ')
if pregunta == 'Si':
    nombre_vendedor = input('Nombre del vendedor: ')
    zona_influencia = input('Zona de influencia: ')
    venta = int(input('Valor de la venta: '))
    Diccionario[nombre_vendedor][zona_influencia] = venta
    print('La información se ha modificado correctamente')
    print(Diccionario)
elif pregunta == 'No':
    pass
else:
    raise ValueError('Respuesta incorrecta. Seleccione Si o No')

claves_internas = []
for cliente, zonas in Diccionario:
    for i in zonas.keys():
        claves_internas.append(i)
print (claves_internas)