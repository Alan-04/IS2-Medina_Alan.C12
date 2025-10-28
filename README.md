# IS2 - Sistema Biblioteca (Alan Medina)

Resumen de la entrega
- Lenguaje: Python
- Patrón elegido para el problema: Singleton (acceso centralizado a la base de datos)
- Estructura del proyecto: ver árbol de carpetas en la entrega

1) Capas del sistema
- Presentación
  - Archivos: src/main.py, test_conexion.py
  - Funciones típicas: interacción con el usuario, mostrar resultados, orquestar llamadas al servicio.
- Lógica de negocio
  - Archivos: src/servicio/servicio_prestamos.py, src/dominio/*
  - Funciones típicas: reglas de préstamo y devolución, validaciones, cálculos (fecha de devolución).
- Datos
  - Archivos: src/conexion_bd.py
  - Funciones típicas: definición de modelos ORM, inicialización del engine y sessionmaker, obtención de sesiones.

2) Problema elegido: acceso centralizado a la base de datos
- Descripción breve:
  El acceso a la base de datos debe ser único y consistente en toda la aplicación para evitar múltiples configuraciones de engine/session, datos inconsistentes y complicaciones en tests y despliegue.
- Patrón elegido: Singleton
- Justificación (en palabras propias):
  La clase ConexionBD implementa Singleton para garantizar una única instancia que inicializa el engine y el sessionmaker. Así todas las capas usan la misma fuente de verdad (misma configuración de conexión y factory de sesiones), simplificando la gestión de la BD y las pruebas.

3) Validación del modelo en Python
- Tests unitarios: anexo/pruebas_unitarias.py (ejecutar `python -m anexo.pruebas_unitarias`)
- Prueba de conexión: test_conexion.py (ejecutar `python test_conexion.py`)
- Nota: si cambias los modelos (unique constraints) borra `biblioteca.db` para que las tablas se recreeen:
  - PowerShell: `Remove-Item .\biblioteca.db -Force`

Instrucciones rápidas
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
