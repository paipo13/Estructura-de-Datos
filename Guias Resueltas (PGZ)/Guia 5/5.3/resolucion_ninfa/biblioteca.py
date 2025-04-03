from libro import Libro
from usuario import Usuario


class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estanteria = [] #Libro
        self.socios = [] #Usuario

    def devolver_a_estanteria(self, libro: Libro):
        self.estanteria.append(libro)

    def agregar_usuario(self, usuario: Usuario):
        self.socios.append(usuario)

    def __str__(self):
        return f"Nombre: {self.nombre}\nLibros: {self.estanteria}"

    def listar_libros(self):
        for i, libro in enumerate(self.estanteria):
            print(f"{i + 1} - {libro}")

    def realizar_prestamo(self, dni: str, titulo: str):
        usuario_solicitante = self.buscar_usuario(dni)
        libro_pedido = self.buscar_libro(titulo)
        self.entregar_libro(usuario_solicitante, libro_pedido)

    def finalizar_prestamo(self, dni: str, titulo: str):
        solicitante = self.buscar_usuario(dni)
        libro = solicitante.entregar_libro(titulo)
        self.devolver_a_estanteria(libro)

    def buscar_libro(self, titulo: str) -> Libro:
        buscado = None
        for libro in self.estanteria:
            if libro.titulo == titulo:
                buscado = libro
        if not buscado:
            raise ValueError("Libro no encontrado")
        return buscado

    def buscar_usuario(self, dni: str) -> Usuario:
        buscado = None
        for usuario in self.socios:
            if usuario.dni == dni:
                buscado = usuario
        if buscado == None:
            raise ValueError("Usuario no encontrado")
        return buscado

    def entregar_libro(self, usuario: Usuario, libro: Libro):
        self.estanteria.pop(self.estanteria.index(libro))
        usuario.tomar_libro(libro)

    def get_estanteria(self):
        return self.estanteria
    