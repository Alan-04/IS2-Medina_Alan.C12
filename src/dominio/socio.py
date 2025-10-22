from src.dominio.prestamo import Prestamo

class Socio:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

    def realizar_prestamo(self, libro):
        """Crea un préstamo para el socio si el libro está disponible."""
        if not libro.disponible:
            raise Exception(f"El libro '{libro.titulo}' no está disponible.")
        libro.marcar_no_disponible()
        return Prestamo(libro=libro, socio=self)
