class ServicioPrestamos:
    def registrar_prestamo(self, socio, libro):
        """Registra un nuevo préstamo."""
        print(f"Registrando préstamo del libro '{libro.titulo}' para {socio.nombre}")
        return socio.realizar_prestamo(libro)

    def registrar_devolucion(self, prestamo):
        """Registra la devolución de un préstamo."""
        prestamo.libro.marcar_disponible()
        print(f"Devolución registrada para el libro '{prestamo.libro.titulo}'")
