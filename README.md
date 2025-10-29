# 📚 Sistema de Gestión de Biblioteca  
**Materia:** Ingeniería de Software II  
**Alumno:** Alan Medina
**Profesor:** Victor Contreras
**Carrera:** Licenciatura en Gestión de Tecnologías de la Información  

---

## 🧩 Descripción del proyecto

Este sistema te permite gestionar una biblioteca digital con funcionalidades, en las cuales se incluyen:
- Registro de libros y socios  
- Préstamo y devolución de libros  
- Control de disponibilidad  
- Persistencia de datos mediante conexión a base de datos
- Lenguaje: Python
- Patrón elegido para el problema: Singleton (acceso centralizado a la base de datos)
- Estructura del proyecto:
```IS2-Medina_Alan.C12/
├── src/
│   ├── __init__.py
│   ├── conexion_bd.py
│   ├── main.py
│   ├── dominio/
│   │   ├── __init__.py
│   │   ├── libro.py
│   │   ├── prestamo.py
│   │   └── socio.py
│   └── servicio/
│       ├── __init__.py
│       └── servicio_prestamos.py
├── anexo/
│   ├── __init__.py
│   └── pruebas_unitarias.py
├── documento/
│   └── diagrama_uml.mmd
├── test_conexion.py
├── README.md
├── requirements.txt
├── .gitignore
└── biblioteca.db
```


El desarrollo se basa en la **arquitectura en tres capas**

---
## 🧱 Arquitectura en tres capas

| **Capa** | **Artefactos / Elementos** | **Responsabilidad** | **Código Fuente** |
|-----------|-----------------------------|----------------------|-------------------|
| **Presentación** | Archivo principal `main.py`. | Es el punto de entrada del sistema. Se encarga de interactuar con el usuario y distribuir las operaciones a las demás capas. | `main.py` |
| **Lógica de Negocio (Dominio)** | Clases de dominio (`libro.py`, `socio.py`, `prestamo.py`). Servicios de negocio (`servicio_prestamos.py`). Artefactos de validación y cálculo (por ejemplo, validación de disponibilidad o control de fechas). Diagramas UML de clases y dominio. | Contiene las reglas del negocio y la lógica interna del sistema (por ejemplo, control de disponibilidad, cálculo de fechas de devolución, registro de préstamos, etc.). Representa las entidades del dominio y coordina la interacción con la capa de datos. | `libro.py`, `socio.py`, `prestamo.py`, `servicio_prestamos.py` |
| **Persistencia (SRC)** | Repositorio de conexión a la base de datos y clases asociadas. | Administra el almacenamiento, gestión y recuperación de los datos. Utiliza SQLAlchemy para manejar la conexión y las operaciones sobre la base de datos relacional. | `conexion_bd.py`, motor de base de datos `SQLAlchemy` |



---

## 🧠 Patrón de Diseño Aplicado: Singleton para el acceso centralizado a la base de datos.

**Problema elegido:**  
Se necesita una única conexión activa a la base de datos para evitar bloqueos o inconsistencias.
- Descripción breve:
  El acceso a la base de datos debe ser único y consistente en toda la aplicación para evitar múltiples configuraciones de engine/session, datos inconsistentes y complicaciones en tests y despliegue.
- Patrón elegido: Singleton
- Explicación de la elección:
  La clase ConexionBD implementa Singleton para garantizar una única instancia que inicializa el engine y el sessionmaker. Así todas las capas usan la misma fuente de verdad (misma configuración de conexión y factory de sesiones), simplificando la gestión de la BD y las pruebas.

**Ventajas:**  
- Evita múltiples conexiones innecesarias  
- Centraliza el acceso a la base de datos  
- Facilita el mantenimiento y control de errores  

**Instrucciones rápidas**
1. Crear entorno virtual
   python -m venv .venv
   .\.venv\Scripts\activate

2. Instalar dependencias
   pip install -r requirements.txt

3. Ejecutar tests
   python -m anexo.pruebas_unitarias

4. Probar conexión
   python test_conexion.py

Archivos:
- src/ (código fuente, ConexionBD, servicios, dominio)
- anexo/pruebas_unitarias.py (tests que pasan)
- diagrama_uml.md (UML)
- test_conexion.py (test de la base de datos)
- .gitignore (evita subir biblioteca.db)