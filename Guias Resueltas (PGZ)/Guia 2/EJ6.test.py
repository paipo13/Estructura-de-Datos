# Escribe una función llamada operaciones, que toma una cadena y una lista como parámetros de entrada.
# Dentro de la función operaciones, se crean funciones que realizan las siguientes tareas:
# a. Contar: Imprime la cantidad de veces que aparece la cadena en la lista.
# b. Modificar: Pide al usuario una segunda cadena para modificar la cadena ingresada como parámetro.
# Modifica todas las apariciones de la primera cadena por la segunda en la lista.
# c. Eliminar: Elimina la cadena ingresada como parámetro de entrada de la lista.

def operaciones(cadena, lista):
    def contar():
        print(f'La cadena "{cadena}" aparece {lista.count(cadena)} veces en la lista.')

    def modificar(cadena2):
        nonlocal cadena  # Declara cadena como nolocal para poder modificarla
        cadena = cadena2  # Actualiza la variable cadena
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