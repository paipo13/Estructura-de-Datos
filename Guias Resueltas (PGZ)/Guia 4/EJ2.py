# Implementen, mediante el paradigma funcional, un sistema de matriculación de alumnos. 
# El sistema debe tener un menú de opciones con las siguientes funcionalidades:
# a-Ver materias disponibles: cada materia está asociada a un índice.
# b-Matricularse a una nueva materia: el usuario ingresa el índice de la materia.
# c-Ver las materias inscritas
# d-Confirmar la inscripción

# El programa debe ser funcional. La información de las materias y la carga horaria
# se carga desde un archivo csv que usted debe definir a modo de ejemplo.
# Debe identificar, enumerar y manejar correctamente cada caso de error en su programa.
def menu():
    materias = ['Mate III', 'Mate II', 'Mate', 'Fisica II', 'Fisica', 'Algebra','Quimica']
    indices_materias = ['1.3','1.2','1.1','2.2','2.1','7,9','5.5']
    cargas_horarias = [10,10,12,8,8,9,9]
    materias_disponibles = ['Mate III', 'Mate II', 'Mate', 'Fisica II', 'Fisica', 'Algebra','Quimica']
    materias_inscriptas = []
    carga_horaria = 0
    print("Bienvenido al sistema de matriculación")
    def cargar_materias(nombre_materia):
        if nombre_materia not in materias:
            pass
    def matriculacion(indice_materia):
        j = 0
        nonlocal carga_horaria
        try:
            for i in range(len(indices_materias)):
                if indices_materias[i] == indice_materia:
                    nombre_materia = materias[i]
                    if nombre_materia in materias_disponibles:
                        materias_inscriptas.append(materias[i])
                        materias_disponibles.remove(nombre_materia)
                        print(f"Se ha matriculado en {nombre_materia}")
                        carga_horaria += float(cargas_horarias[i])
                        print(f"Carga horaria acumulada: {carga_horaria}")
                        j += 1
            if j == 0:
                    print("La materia no está disponible")
        except IndexError:
            print("Error: El índice de materia ingresado no existe.")
        except ValueError:
            print("Error: La carga horaria debe ser un número.")
        except:
            print("Error desconocido")
    while True:
        print("1. Ver materias disponibles")
        print("2. Matricularse a una nueva materia")
        print("3. Ver las materias inscritas")
        print("4. Confirmar la inscripción")
        print("5. Salir")
        eleccion = input("Ingrese su opción: ")
        if eleccion == "1":
            print('Materias disponibles:')
            for i in materias_disponibles:
                print (i)
        elif eleccion == "2":
            indice_materia = (input("Ingrese el índice de la materia: "))
            matriculacion(indice_materia)
        elif eleccion == "3":
            print("Materias inscritas:")
            for materia in materias_inscriptas:
                print(materia)
        elif eleccion == "4":
            pass
        elif eleccion == "5":
            break
        else:
            print("Opción inválida")

menu()
