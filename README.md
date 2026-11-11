# crud-comercio-python
# Trabajo Práctico: Aplicación CRUD con Python y PostgreSQL

Repositorio correspondiente al desarrollo de un sistema de operaciones CRUD (Crear, Leer, Actualizar y Borrar) que integra Python con una base de datos relacional en PostgreSQL.

# Tecnologías Utilizadas
* Lenguaje de programación: Python
* Sistema de gestión de base de datos: PostgreSQL
* Librería de conectividad: `psycopg2-binary`
* Entorno de desarrollo: Visual Studio Code / pgAdmin 4

Estructura del Proyecto
El sistema se encuentra modularizado en tres componentes independientes de acuerdo con el esquema relacional de la base de datos `comercio`:
1. `crud_clientes.py`: Gestión integral de registros en la tabla clientes (atributos: nombre, email, ciudad).
2. `crud_productos.py`: Gestión integral de registros en la tabla productos (atributos: nombre, precio, stock).
3. `crud_pedidos.py`: Gestión de registros en la tabla pedidos con manejo de claves foráneas vinculadas a clientes y productos (atributos: id_cliente, id_producto, cantidad, fecha).

Instrucciones de Ejecución
1. Verificar que PostgreSQL se encuentre en ejecución y que la base de datos `comercio` esté correctamente configurada.
2. Instalar la librería de conexión requerida en el entorno mediante la terminal:
   ```bash
   pip install psycopg2-binary
