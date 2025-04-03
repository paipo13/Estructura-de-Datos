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

