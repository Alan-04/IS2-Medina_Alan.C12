# 🧩 Proyecto: Sistema de Gestión de Biblioteca  
**Materia:** Ingeniería de Software II  
**Alumno:** Alan Medina  
**Curso:** C12  
**Año:** 2025  

---

## 📁 Estructura del Proyecto

```plaintext
IS2-Fulano.Javier.C12/
├── documento/         # Informe técnico y diagrama UML
│   └── informe.md
│
├── src/               # Código fuente del sistema
│   ├── libro.py
│   ├── socio.py
│   ├── prestamo.py
│   └── servicio_prestamos.py
│
└── anexos/            # Archivos adicionales, pruebas y reportes
    └── pruebas_unitarias.py

🚀 Descripción del Sistema

El sistema permite gestionar préstamos y devoluciones de libros dentro de una biblioteca.
Cada préstamo está asociado a un socio y a un libro, con una fecha de devolución automática.

El proyecto aplica los siguientes conceptos clave de Ingeniería de Software II:

Arquitectura en 3 capas (presentación, servicio, dominio).

Patrón de diseño Singleton.

Pruebas unitarias con unittest.

Documentación estructurada y diagrama UML integrable en GitHub.

⚙️ Instalación y Ejecución
1️⃣ Clonar el repositorio
git clone https://github.com/usuario/IS2-Fulano.Javier.C12.git
cd IS2-Fulano.Javier.C12

2️⃣ Ejecutar el sistema

Desde la carpeta raíz:

python src/main.py

3️⃣ Ejecutar las pruebas unitarias
python -m unittest anexos/pruebas_unitarias.py

🧱 Arquitectura del Sistema
flowchart TD
    A[Interfaz / Main] --> B[ServicioPrestamos]
    B --> C[Prestamo]
    C --> D[Libro]
    C --> E[Socio]

    classDef capaA fill:#e0f7fa,stroke:#00acc1,stroke-width:2px;
    classDef capaB fill:#fff3e0,stroke:#fb8c00,stroke-width:2px;
    classDef capaC fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px;

    class A capaA;
    class B capaB;
    class C,E,D capaC;


💡 Leyenda de colores
🩵 Azul = Interfaz
🟧 Naranja = Lógica de negocio
💜 Violeta = Entidades del dominio

🧠 Patrón de Diseño: Singleton

Se aplicó el patrón Singleton para garantizar que solo exista una instancia de conexión a la base de datos o servicio compartido en todo el sistema.

class ConexionBD:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.conectar()
        return cls._instancia

    def conectar(self):
        self.conexion = "Conexión establecida"

🧩 Diagrama UML (GitHub compatible)
classDiagram
    class ServicioPrestamos {
        +registrar_prestamo(socio: Socio, libro: Libro) : Prestamo
        +registrar_devolucion(prestamo: Prestamo) : None
    }

    class Socio {
        -nombre: str
        -email: str
        +realizar_prestamo(libro: Libro) : Prestamo
    }

    class Prestamo {
        -id: int
        -libro: Libro
        -socio: Socio
        -fecha_prestamo: date
        -fecha_devolucion: date
        +calcular_fecha_devolucion() : date
        +esta_vencido() : bool
    }

    class Libro {
        -titulo: str
        -autor: str
        -disponible: bool
        +marcar_no_disponible() : None
        +marcar_disponible() : None
    }

    ServicioPrestamos --> Socio : usa
    ServicioPrestamos --> Libro : usa
    Socio --> Prestamo : realiza
    Prestamo --> Libro : contiene

🧪 Pruebas Unitarias

El archivo anexos/pruebas_unitarias.py contiene las pruebas que validan:

Registro y devolución de préstamos.

Verificación de disponibilidad de libros.

Cálculo de fechas de vencimiento.

Ejemplo:

import unittest
from src.servicio_prestamos import ServicioPrestamos
from src.libro import Libro
from src.socio import Socio

class TestPrestamos(unittest.TestCase):
    def test_prestamo_disponible(self):
        libro = Libro("1984", "George Orwell")
        socio = Socio("Juan Pérez", "juan@example.com")
        servicio = ServicioPrestamos()
        prestamo = servicio.registrar_prestamo(socio, libro)
        self.assertFalse(libro.disponible)