from src.conexion_bd import ConexionBD, Libro, Socio, Prestamo
from datetime import date

# Obtener conexión (Singleton)
conexion = ConexionBD()
sesion = conexion.obtener_sesion()

# Limpiar antes de insertar (evita duplicados al correr repetidamente)
sesion.query(Prestamo).delete()
sesion.query(Libro).delete()
sesion.query(Socio).delete()
sesion.commit()

# ====== Insertar datos de prueba ======
libro1 = Libro(titulo="El Principito", autor="Antoine de Saint-Exupéry", disponible=True)
socio1 = Socio(nombre="Juan Pérez", email="juan@example.com")

sesion.add_all([libro1, socio1])
sesion.commit()

# ejemplo con merge (inserta o actualiza según PK)
sesion.merge(libro1)
sesion.merge(socio1)
sesion.commit()

# ====== Crear un préstamo ======
prestamo1 = Prestamo(
    id_libro=libro1.id,
    id_socio=socio1.id,
    fecha_prestamo=date.today(),
    fecha_devolucion=None
)
sesion.add(prestamo1)
sesion.commit()

# ====== Consultar datos ======
print("\n📚 Libros registrados:")
for libro in sesion.query(Libro).all():
    print(f"{libro.id} - {libro.titulo} ({libro.autor})")

print("\n👥 Socios registrados:")
for socio in sesion.query(Socio).all():
    print(f"{socio.id} - {socio.nombre} ({socio.email})")

print("\n🔁 Préstamos:")
for prestamo in sesion.query(Prestamo).all():
    print(f"Libro ID: {prestamo.id_libro}, Socio ID: {prestamo.id_socio}, Fecha: {prestamo.fecha_prestamo}")

# cerrar sesión al terminar
sesion.close()
