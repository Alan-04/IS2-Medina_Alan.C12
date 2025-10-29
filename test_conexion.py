from src.conexion_bd import ConexionBD, Libro, Socio, Prestamo
from datetime import date, timedelta

# Conexión (Singleton)
conexion = ConexionBD()
sesion = conexion.obtener_sesion()

sesion.query(Prestamo).delete()
sesion.query(Libro).delete()
sesion.query(Socio).delete()
sesion.commit()

# Libros
libros = [
    Libro(titulo="Los juegos del hambre", autor="Suzanne Collins", disponible=True),
    Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", disponible=True),
    Libro(titulo="El principito", autor="Antoine de Saint-Exupéry", disponible=True),
    Libro(titulo="1984", autor="George Orwell", disponible=True),
    Libro(titulo="Harry Potter y la piedra filosofal", autor="J.K. Rowling", disponible=True),
    Libro(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes", disponible=True)
]

# Socios
socios = [
    Socio(nombre="Sergio Moles Montes", email="sergio@example.com"),
    Socio(nombre="Lucía Fernández", email="lucia.fernandez@example.com"),
    Socio(nombre="Martín Gómez", email="martin.gomez@example.com"),
    Socio(nombre="Ana Rodríguez", email="ana.rodriguez@example.com"),
    Socio(nombre="Carlos Pérez", email="carlos.perez@example.com"),
    Socio(nombre="Julieta Díaz", email="julieta.diaz@example.com")
]

sesion.add_all(libros + socios)
sesion.commit()

for libro in libros:
    sesion.merge(libro)
for socio in socios:
    sesion.merge(socio)
sesion.commit()

prestamos = [
    Prestamo(id_libro=libros[0].id, id_socio=socios[0].id, fecha_prestamo=date.today(), fecha_devolucion=None),
    Prestamo(id_libro=libros[1].id, id_socio=socios[1].id, fecha_prestamo=date.today() - timedelta(days=3), fecha_devolucion=None),
    Prestamo(id_libro=libros[2].id, id_socio=socios[2].id, fecha_prestamo=date.today() - timedelta(days=10), fecha_devolucion=date.today() - timedelta(days=2)),
    Prestamo(id_libro=libros[3].id, id_socio=socios[3].id, fecha_prestamo=date.today() - timedelta(days=1), fecha_devolucion=None),
    Prestamo(id_libro=libros[4].id, id_socio=socios[4].id, fecha_prestamo=date.today() - timedelta(days=7), fecha_devolucion=None),
    Prestamo(id_libro=libros[5].id, id_socio=socios[5].id, fecha_prestamo=date.today(), fecha_devolucion=None)
]

sesion.add_all(prestamos)
sesion.commit()

# Resultados:
print("\n📚 Libros registrados:")
for libro in sesion.query(Libro).all():
    print(f"{libro.id} - {libro.titulo} ({libro.autor})")

print("\n👥 Socios registrados:")
for socio in sesion.query(Socio).all():
    print(f"{socio.id} - {socio.nombre} ({socio.email})")

print("\n🔁 Préstamos:")
for prestamo in sesion.query(Prestamo).all():
    print(f"Libro ID: {prestamo.id_libro}, Socio ID: {prestamo.id_socio}, Fecha: {prestamo.fecha_prestamo}, "
          f"Devolución: {prestamo.fecha_devolucion}")

sesion.close()
