import unittest
from datetime import date, timedelta
from src.conexion_bd import ConexionBD, Libro, Socio
from src.servicio.servicio_prestamos import ServicioPrestamos

class TestSistemaBiblioteca(unittest.TestCase):
    def setUp(self):
        self.db = ConexionBD()
        self.session = self.db.obtener_sesion()
        self.session.query(Libro).delete()
        self.session.query(Socio).delete()
        self.session.commit()

        self.libro = Libro(titulo="Los juegos del hambre", autor="Suzanne Collins", disponible=True)
        self.socio = Socio(nombre="Sergio Moles Montes", email="SergioMM@example.com")

        self.session.add_all([self.libro, self.socio])
        self.session.commit()

        self.servicio = ServicioPrestamos()

    def test_registrar_prestamo(self):
        prestamo = self.servicio.registrar_prestamo(self.socio, self.libro)
        libro_actualizado = self.session.get(Libro, self.libro.id)
        self.assertFalse(libro_actualizado.disponible)
        self.assertEqual(prestamo.libro.id, self.libro.id)


    def test_calcular_fecha_devolucion(self):
        prestamo = self.servicio.registrar_prestamo(self.socio, self.libro)
        esperado = date.today() + timedelta(days=7)
        self.assertTrue(prestamo.fecha_prestamo <= esperado)

    def test_registrar_devolucion(self):
        prestamo = self.servicio.registrar_prestamo(self.socio, self.libro)
        prestamo_actualizado = self.servicio.registrar_devolucion(prestamo)
        self.assertTrue(prestamo_actualizado.libro.disponible)

    def tearDown(self):
        self.session.close()


if __name__ == "__main__":
    unittest.main()
