# 📚 Sistema de Gestión de Biblioteca  
**Materia:** Ingeniería de Software II  
**Alumno:** Alan Medina – C12  
**Carrera:** Licenciatura en Gestión de Tecnologías de la Información  

---

## 🧩 Descripción del proyecto

El sistema permite gestionar una biblioteca digital con funcionalidades básicas como:
- Registro de libros y socios  
- Préstamo y devolución de libros  
- Control de disponibilidad  
- Persistencia de datos mediante conexión a base de datos  

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

**Problema identificado:**  
Se necesita una única conexión activa a la base de datos para evitar bloqueos o inconsistencias.

**Solución:**  
Se implementó el **patrón Singleton** en la clase `ConexionBD`, que garantiza que solo exista una instancia compartida de la conexión a la base de datos.

**Ventajas:**  
- Evita múltiples conexiones innecesarias  
- Centraliza el acceso a la base de datos  
- Facilita el mantenimiento y control de errores  

### 📄 Ejemplo del patrón Singleton

```python
from src.conexion_bd import ConexionBD

db1 = ConexionBD()
db2 = ConexionBD()

print(db1 is db2)  # ✅ True — ambas variables apuntan a la misma instancia
