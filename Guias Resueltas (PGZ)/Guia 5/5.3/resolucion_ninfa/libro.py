class Libro:
    def __init__(self, titulo: str, autor: str, editorial: str):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.editorial}"

