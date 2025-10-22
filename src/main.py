from dominio.libro import Libro
from dominio.socio import Socio
from servicio.servicio_prestamos import ServicioPrestamos

if __name__ == "__main__":
    # Capa de Presentación / Ejemplo de uso
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    socio1 = Socio("Alan Medina", "alan@example.com")

    servicio = ServicioPrestamos()

    # Registrar préstamo
    prestamo = servicio.registrar_prestamo(socio1, libro1)
    print(f"Fecha de devolución: {prestamo.fecha_devolucion}")
    print(f"¿Está vencido? {prestamo.esta_vencido()}")

    # Registrar devolución
    servicio.registrar_devolucion(prestamo)
    print(f"¿El libro '{libro1.titulo}' está disponible? {libro1.disponible}")