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
IS2-Medina_Alan.C12/
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

El desarrollo se basa en la **arquitectura en tres capas** y la aplicación del **patrón de diseño Singleton** para el acceso centralizado a la base de datos.

---

## 🏗️ Arquitectura en tres capas

| **Capa** | **Responsabilidad** | **Ejemplo de archivo / clase** |
|-----------|---------------------|--------------------------------|
| **Presentación** | Interfaz con el usuario o punto de entrada del sistema. | `main.py` |
| **Lógica de negocio (Dominio)** | Contiene las reglas del sistema y entidades. | `libro.py`, `socio.py`, `prestamo.py` |
| **Datos (Persistencia)** | Administra el almacenamiento y acceso a la base de datos. | `conexion_bd.py`, `servicio_prestamos.py` |

---

## 🧠 Patrón de Diseño Aplicado: Singleton

**Problema elegido:**  
Se necesita una única conexión activa a la base de datos para evitar bloqueos o inconsistencias.
- Descripción breve:
  El acceso a la base de datos debe ser único y consistente en toda la aplicación para evitar múltiples configuraciones de engine/session, datos inconsistentes y complicaciones en tests y despliegue.
- Patrón elegido: Singleton
- Justificación:
  La clase ConexionBD implementa Singleton para garantizar una única instancia que inicializa el engine y el sessionmaker. Así todas las capas usan la misma fuente de verdad (misma configuración de conexión y factory de sesiones), simplificando la gestión de la BD y las pruebas.

**Ventajas:**  
- Evita múltiples conexiones innecesarias  
- Centraliza el acceso a la base de datos  
- Facilita el mantenimiento y control de errores  

**Instrucciones rápidas**
1. Crear entorno virtual (opcional)
   python -m venv .venv
   .\.venv\Scripts\activate

2. Instalar dependencias
   pip install -r requirements.txt

3. Ejecutar tests
   python -m anexo.pruebas_unitarias

4. Probar conexión
   python test_conexion.py

Archivos incluidos en la entrega
- src/ (código fuente, ConexionBD, servicios, dominio)
- anexo/pruebas_unitarias.py (tests que pasan)
- diagrama_uml.mmd (UML)
- test_conexion.py (script de verificación)
- .gitignore (excluye biblioteca.db)


