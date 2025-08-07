# Hay muchos tipos de errores que pupede generar el sistema entre ellos podemos encontrar:
# 1. ZeroDivisionError
# 2. TypeError
# 3. ValueError
# 4. FileNotFoundError
# 5. IndententionError
# 5. etc...

# Ejemplo 1: ZeroDivisionError
x=1000
seguir=True
while seguir==True:
    try:
        y=int(input("ingrese un dato diferente de CERO "))  
        if x<2000:
            if y !=0:
                print(x/y)
                seguir=False

            else:
                raise ZeroDivisionError ("Division por cero")
        else:
            print("Puedes hacer tus compras")
            seguir=False

    except ZeroDivisionError as e:
        print("El error que ha ocurrido es ", e)
    except ValueError:
        print("El dato introducido no corresponde al valor esperado")







# Ejemplo 2: TypeError
try:
    numero=int(input("Ingresa un numero"))
    cantidadDigitos=len(numero)
    print(cantidadDigitos)
    
except TypeError as e:
    print('Esta haciendo una operacion no valida')
    print(e)

else:
    print('No hubo error')
       
finally: #El finally se printea en la terminal siempre
    print('hubo o no hubo ERROR')




# Ejemplo 3: ValueError
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    elif edad > 120:
        raise ValueError("La edad no puede ser mayor a 120 años.")
    else:
        print(f"La edad ingresada es válida: {edad}")

# Example usage
try:
    edad = int(input("Ingrese su edad: "))
    validar_edad(edad)
except ValueError as e:
    print(f"Error: {e}")






# Ejemplo 4: FileNotFoundError
#ABRIR UN ARCHIVO EXISTENTE EN MI MAQUINA
import traceback
from io import UnsupportedOperation


def existe(patharchivo):
    try:
        archivo=open(patharchivo,'w')
        archivo.write("Hola como estas")
        return archivo
    except FileNotFoundError:
        traceback.print_exc()
        return None
    except UnsupportedOperation:
        print("El archivo esta tratando de realizar una tarea no permitida")
    

if __name__=="__main__":
    patharchivo=r"C:\Users\ninfa\OneDrive\Documentos\Cuatrimestre 1 2022\Materia 71.45 Estructuras\Ejemplos_EstructurasDatos\matriz.txt"
    manejararchivo=existe(patharchivo)
    if manejararchivo!= None:
        print("Archivo Existe")
        for linea in manejararchivo:
            print(linea)
    else:
        print("El archivo no existe")





# Ejemplo 5: IndententionError
x=1000
if x<2000:
    print("Ese dinero disponible no es sufuciente para una compra")
else:
    print("vamos de compras")




# Ejemplo del uso de distintos niveles de try:
try:
    # Primer nivel de try
    print("Primer nivel try")
    x = 10 / 2 

    try:
        # Segundo nivel de try
        print("Segundo nivel try")
        y = 5 / 0  # Esto causará un ZeroDivisionError

    except ZeroDivisionError as e:
        print(f"Excepción atrapada en el segundo nivel: {e}")

        try:
            # Tercer nivel de try
            print("Tercer nivel try")
            z = int("no es un número")  # Esto causará un ValueError

        except ValueError as e:
            print(f"Excepción atrapada en el tercer nivel: {e}")

except Exception as e:
    print(f"Excepción atrapada en el primer nivel: {e}")

print("Programa finalizado.")


### Buenas Practicas de exepciones ###

# Una buena practica para las exepciones es aplicar un Raise