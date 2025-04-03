# Escriba una función llamada operaciones, que tenga como parámetro de entrada una cadena y una lista la
# cual puede almacenar en cada elemento una o más palabras.
# Dentro de la función operaciones deben ser creadas las funciones que hacen las siguientes tareas:
# a. Contar: Debe imprimir la cantidad de veces que aparece la cadena en la lista
# b. Modificar: Se pide al usuario una segunda cadena para modificar la cadena ingresada como
# parámetro, debe modificar todas las apariciones de la primera cadena por la segunda en la lista.
# c. Eliminar: Eliminar la cadena ingresada como parámetro de entrada en la lista
# Debe tener presente que los cambios realizados a la lista a medida que se ejecutan cada una de las
# funciones internas, no son permanentes es decir que al ejecutar cada función interna de la función
# Operaciones se debe usar la lista inicial siempre.


def operaciones(cadena, lista):
    def contar():
        print(f'La cadena "{cadena}" aparece {lista.count(cadena)} veces en la lista.')

    def modificar(cadena2):
        nonlocal cadena 
        cadena = cadena2
        lista[:] = [cadena2 if palabra == cadena else palabra for palabra in lista]
        print(f'La cadena "{cadena}" ha sido modificada por "{cadena2}" en la lista.')
        print(lista)

    def eliminar():
        lista[:] = [palabra for palabra in lista if palabra != cadena]
        print(f'La cadena "{cadena}" ha sido eliminada de la lista.')
        print(lista)
    
    def menu():
        while True:
            print('1. Contar')
            print('2. Modificar')
            print('3. Eliminar')
            print('4. Salir')
            
            opcion = input('Ingrese una opción: ')
            
            if opcion == '1':
                contar()
            elif opcion == '2':
                modificar(input('Ingrese la segunda cadena: '))
            elif opcion == '3':
                eliminar()
            elif opcion == '4':
                break
            else:
                print('Opción inválida.')
            
    menu()

cadena = 'olaf'
lista = [1,3,4,['ujo','olaf',78],'olaf','olaf','olaf','chain']

operaciones(cadena, lista)