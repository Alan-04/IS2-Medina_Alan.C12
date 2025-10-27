from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class ConexionBD:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia

    def _inicializar(self):
        """Inicializa la conexión con SQLAlchemy (una sola vez)."""
        self.engine = create_engine("sqlite:///biblioteca.db", echo=False)
        # Evitar que SQLAlchemy expire los atributos al hacer commit,
        # así los objetos devueltos conservan sus valores aunque la sesión se cierre.
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)
        Base.metadata.create_all(self.engine)

    def obtener_sesion(self):
        return self.Session()


# =======================
# MODELOS ORM
# =======================

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    autor = Column(String)
    disponible = Column(Boolean, default=True)

    # 🔹 Relación hacia Prestamo
    prestamos = relationship("Prestamo", back_populates="libro")

    def marcar_no_disponible(self):
        self.disponible = False

    def marcar_disponible(self):
        self.disponible = True


class Socio(Base):
    __tablename__ = "socios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    email = Column(String)

    # 🔹 Relación hacia Prestamo
    prestamos = relationship("Prestamo", back_populates="socio")


class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_libro = Column(Integer, ForeignKey("libros.id"))
    id_socio = Column(Integer, ForeignKey("socios.id"))
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date, nullable=True)

    # 🔹 Relaciones hacia Libro y Socio
    libro = relationship("Libro", back_populates="prestamos")
    socio = relationship("Socio", back_populates="prestamos")
