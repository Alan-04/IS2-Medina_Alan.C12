from datetime import date, timedelta

class Prestamo:
    def __init__(self, libro, socio):
        self.id = id(self)
        self.libro = libro
        self.socio = socio
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.calcular_fecha_devolucion()

    def calcular_fecha_devolucion(self):
        """Calcula la fecha de devolución (7 días después)."""
        return self.fecha_prestamo + timedelta(days=7)

    def esta_vencido(self):
        """Verifica si el préstamo está vencido."""
        return date.today() > self.fecha_devolucion
