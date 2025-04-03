from libro import Libro

class Usuario:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.mochila = []

    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}"

    def listar_prestados(self):
        for i, libro in enumerate(self.mochila):
            print(f"{i + 1} - {libro}")

    def entregar_libro(self, titulo: str) -> Libro:
        buscado = None
        for indice, libro in enumerate(self.mochila):
            if libro.titulo == titulo:
                buscado = indice
        if buscado == None:
            raise ValueError("libro no encontrado")
        return self.mochila.pop(buscado)

    def tomar_libro(self, libro: Libro):
        self.mochila.append(libro)
