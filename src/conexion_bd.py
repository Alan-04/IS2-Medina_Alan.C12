from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Date, UniqueConstraint
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
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)
        Base.metadata.create_all(self.engine)

    def obtener_sesion(self):
        return self.Session()

# MODELOS ORM:
class Libro(Base):
    __tablename__ = "libros"
    __table_args__ = (UniqueConstraint('titulo', 'autor', name='uix_titulo_autor'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    autor = Column(String)
    disponible = Column(Boolean, default=True)

    prestamos = relationship("Prestamo", back_populates="libro")

    def marcar_no_disponible(self):
        self.disponible = False

    def marcar_disponible(self):
        self.disponible = True

    def __repr__(self):
        return f"<Libro id={self.id} titulo={self.titulo!r} disponible={self.disponible}>"


class Socio(Base):
    __tablename__ = "socios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    email = Column(String, unique=True)

    prestamos = relationship("Prestamo", back_populates="socio")

    def __repr__(self):
        return f"<Socio id={self.id} nombre={self.nombre!r} email={self.email!r}>"


class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_libro = Column(Integer, ForeignKey("libros.id"))
    id_socio = Column(Integer, ForeignKey("socios.id"))
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date, nullable=True)

    libro = relationship("Libro", back_populates="prestamos")
    socio = relationship("Socio", back_populates="prestamos")

    def __repr__(self):
        return f"<Prestamo id={self.id} libro_id={self.id_libro} socio_id={self.id_socio} fecha_prestamo={self.fecha_prestamo}>"
