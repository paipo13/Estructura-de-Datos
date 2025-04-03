# is es una palabra reservada de Python que permite determinar si dos objetos son iguales, basado en esta 
# definición que valor se obtendrá de las siguientes expresiones:
profe= "Agostina"
mi_profe= "Agostina"
print(profe is mi_profe)
pro= "Agostina?"
pro_Agos= "Agostina?"
print(pro is pro_Agos)
a="a"
b="b"
print(a is b)
ver="!"
ver_mas="!"
print(ver is ver_mas)
numero1=120
numero2=120
print(numero1 is numero2)
numero1=12000000
numero2=12000000
print(numero1 is numero2)
print(id(numero1))
print(id(numero2))