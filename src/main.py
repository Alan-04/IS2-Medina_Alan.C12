from datetime import date
from src.conexion_bd import Libro, Socio
from src.servicio.servicio_prestamos import ServicioPrestamos

def demo():
    servicio = ServicioPrestamos()

    libro = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", disponible=True)
    socio = Socio(nombre="Alan Medina", email="alan@example.com")

    prestamo = servicio.registrar_prestamo(socio, libro)
    print("Fecha préstamo:", prestamo.fecha_prestamo)
    print("Fecha devolución calculada (ej.):", servicio.calcular_fecha_devolucion(prestamo))
    print("¿Está vencido?", (date.today() > servicio.calcular_fecha_devolucion(prestamo)))

    prestamo = servicio.registrar_devolucion(prestamo)
    print(f"¿El libro '{prestamo.libro.titulo}' está disponible? {prestamo.libro.disponible}")

if __name__ == "__main__":
    demo()