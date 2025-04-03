'''numero=int(input("Ingresa un numero"))
cantidadDigitos=len(numero)
print(cantidadDigitos)'''

try:
    numero=int(input("Ingresa un numero"))
    cantidadDigitos=len(numero)
    print(cantidadDigitos)
    
except TypeError as e:
    print('Esta haciendo una operacion no valida')
    print(e)

else:
    print('No hubo error')
       
finally:
    print('hubo o no hubo ERROR')


    