from datetime import date, timedelta
from src.conexion_bd import ConexionBD, Prestamo

class ServicioPrestamos:
    def __init__(self):
        self.conexion = ConexionBD()

    def registrar_prestamo(self, socio, libro):
        """Registra un nuevo préstamo si el libro está disponible."""
        if not libro.disponible:
            raise Exception("El libro no está disponible para préstamo.")
        libro.disponible = False
        sesion = self.conexion.obtener_sesion()
        try:
            socio_db = sesion.merge(socio)
            libro_db = sesion.merge(libro)
            prestamo_db = Prestamo(
                libro=libro_db,
                socio=socio_db,
                fecha_prestamo=date.today(),
                fecha_devolucion=None
            )
            sesion.add(prestamo_db)
            sesion.commit()
            sesion.refresh(prestamo_db)
            prestamo_db.libro = libro_db
            sesion.expunge(prestamo_db)
            sesion.expunge(libro_db)
            return prestamo_db

        except Exception:
            sesion.rollback()
            raise
        finally:
            sesion.close()

    def registrar_devolucion(self, prestamo):
        if hasattr(prestamo, "libro") and prestamo.libro is not None:
            prestamo.libro.disponible = True

        sesion = self.conexion.obtener_sesion()
        try:
            prestamo_db = sesion.merge(prestamo)
            prestamo_db.fecha_devolucion = date.today()
            prestamo_db.libro.disponible = True
            sesion.commit()
            sesion.refresh(prestamo_db)
            sesion.refresh(prestamo_db.libro)
            sesion.expunge(prestamo_db)
            sesion.expunge(prestamo_db.libro)
            return prestamo_db

        except Exception:
            sesion.rollback()
            raise
        finally:
            sesion.close()

    def calcular_fecha_devolucion(self, prestamo, dias_prestamo=7):
        return prestamo.fecha_prestamo + timedelta(days=dias_prestamo)