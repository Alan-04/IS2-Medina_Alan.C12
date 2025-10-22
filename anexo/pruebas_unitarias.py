import unittest
from datetime import date, timedelta
from src.dominio.libro import Libro
from src.dominio.socio import Socio
from src.servicio.servicio_prestamos import ServicioPrestamos

class TestSistemaBiblioteca(unittest.TestCase):

    def setUp(self):
        self.libro = Libro("El Principito", "Antoine de Saint-Exupéry")
        self.socio = Socio("Lucía Pérez", "lucia@example.com")
        self.servicio = ServicioPrestamos()

    def test_registrar_prestamo(self):
        prestamo = self.servicio.registrar_prestamo(self.socio, self.libro)
        self.assertFalse(self.libro.disponible)
        self.assertEqual(prestamo.libro.titulo, "El Principito")

    def test_calcular_fecha_devolucion(self):
        prestamo = self.servicio.registrar_prestamo(self.socio, self.libro)
        esperado = date.today() + timedelta(days=7)
        self.assertEqual(prestamo.fecha_devolucion, esperado)

    def test_registrar_devolucion(self):
        prestamo = self.servicio.registrar_prestamo(self.socio, self.libro)
        self.servicio.registrar_devolucion(prestamo)
        self.assertTrue(self.libro.disponible)

if __name__ == '__main__':
    unittest.main()
