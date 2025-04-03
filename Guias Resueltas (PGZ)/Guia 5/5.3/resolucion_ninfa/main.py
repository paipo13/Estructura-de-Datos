from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario
from exportador import Exportador, ExportadorBiblioteca

if __name__ == '__main__':
    libro1 = Libro("El Principito", "Saint Exupery", "Salamandra")
    libro2 = Libro("Los versos del Capitán", "Pablo Neruda", "Planeta")
    libro3 = Libro("El cantar de los nibelungos", "Varios autores", "Ediciones Akal")

    usuario1 = Usuario("Carlos", "11111111")
    usuario2 = Usuario("Franco", "22222222")
    usuario3 = Usuario("Maria", "33333333")

    biblioteca = Biblioteca("Biblioteca Popular")


    biblioteca.devolver_a_estanteria(libro1)
    biblioteca.devolver_a_estanteria(libro2)
    biblioteca.devolver_a_estanteria(libro3)
    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(usuario2)
    biblioteca.agregar_usuario(usuario3)

    print(f"{' Abre la biblioteca ':#^40}")
    biblioteca.listar_libros()
    print()
    print()
    print(f"{' Carlos pide un libro ':#^40}")
    biblioteca.realizar_prestamo(usuario1.dni, "El Principito")
    biblioteca.listar_libros()
    print()
    print()
    print(f"{' Libros de Carlos ':#^40}")
    usuario1.listar_prestados()
    print()
    print()
    print(f"{' Carlos devuelve un libro ':#^40}")
    biblioteca.finalizar_prestamo("11111111", "El Principito")
    biblioteca.listar_libros()

    exportadorB = ExportadorBiblioteca(f"{biblioteca.nombre}.csv")
    exportadorB.exportar(biblioteca)

    exportadorL = Exportador("letras.csv")
    exportadorL.exportar([["a","b","c"],
                         ["d","e","f"]])





