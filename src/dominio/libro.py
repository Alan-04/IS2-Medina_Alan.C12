class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def marcar_no_disponible(self):
        """Marca el libro como no disponible."""
        self.disponible = False

    def marcar_disponible(self):
        """Marca el libro como disponible nuevamente."""
        self.disponible = True
