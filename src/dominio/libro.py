class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def marcar_no_disponible(self):
        self.disponible = False

    def marcar_disponible(self):
        self.disponible = True
