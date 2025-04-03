# Escriba una función que dado un conjunto de diccionarios (clave: string, contenido: real) 
# devuelva un único diccionario (clave: string, valor conjunto de reales).
# Ejemplo 1
# {{“Pan”:22.8,”Pollo”:33.85},
# {“Mermelada”:42.5, “Pan”:23.55,”Tomate”:18.3},
# {“Pan”:28.0,”Tomate”:19.5,”Pollo”:34.6}}

# La función debe devolver:
# {“Pan”:{22.8,23.5,28},
# “Mermelada”:{42.5},
# ”Tomate”:{18.3,19.5},
# “Pollo”:{33.85,34.6}}

def conjunto_diccionarios_separados(diccionario1, diccionario2, diccionario3):
    diccionario_final = {}
    for diccionario in [diccionario1, diccionario2, diccionario3]:
        for clave, valor in diccionario.items():
            if clave in diccionario_final:
                diccionario_final[clave].add(valor)
            else:
                diccionario_final[clave] = {valor}
    return diccionario_final

diccionario1 = {'Pan':22.8,'Pollo':33.85}
diccionario2 = {'Mermelada':42.5, 'Pan':23.55,'Tomate':18.3}
diccionario3 =  {'Pan':28.0,'Tomate':19.5,'Pollo':34.6}

print(conjunto_diccionarios_separados(diccionario1, diccionario2, diccionario3))

def diccionario_con_diccionarios(diccionario):
    diccionario_final = {}
    for clave,valor in diccionario.items():
        for clave1,valor1 in valor.items():
            if clave1 not in diccionario_final:
                diccionario_final[clave1] = {valor1}
            else:
                diccionario_final[clave1].add(valor1)
    return diccionario_final

diccionario_con_diccionario = {'A':{'Pan':22.8,'Pollo':33.85},'B':{'Mermelada':42.5, 'Pan':23.55,'Tomate':18.3}
                                ,'C':{'Pan':28.0,'Tomate':19.5,'Pollo':34.6}}

print(diccionario_con_diccionarios(diccionario_con_diccionario))
