# 🧪 Casos de prueba – Sistema de Biblioteca

## Función: registrar_prestamo()
- **Tipo de prueba:** Caja negra
- **Caso 1:** Libro disponible → préstamo exitoso  
- **Caso 2:** Libro no disponible → error al crear préstamo  

## Función: calcular_fecha_devolucion()
- **Tipo de prueba:** Caja blanca  
- **Caso 1:** Fecha actual + 7 días → devuelve fecha correcta  

## Función: esta_vencido()
- **Tipo de prueba:** Valores límite  
- **Caso 1:** Fecha actual igual a devolución → No vencido  
- **Caso 2:** Fecha posterior → Vencido  

## Función: registrar_devolucion()
- **Tipo de prueba:** Prueba unitaria  
- **Caso 1:** Libro vuelve a estar disponible después de devolución
