import psycopg2

class GestorPedidos:
    """Clase que agrupa todas las operaciones sobre la tabla pedidos."""

    # -- Constructor: se conecta a la base al crear el objeto --
    def __init__(self, host, port, dbname, user, password):
        self.conexion = psycopg2.connect(
            host=host, port=port, dbname=dbname,
            user=user, password=password
        )
        self.cursor = self.conexion.cursor()
        print("Conexion exitosa a la base de datos (Pedidos)")

    # -- CREATE: insertar un pedido nuevo --
    def crear(self, id_cliente, id_producto, cantidad):
        try:
            self.cursor.execute(
                "INSERT INTO pedidos (id_cliente, id_producto, cantidad) VALUES (%s, %s, %s)",
                (id_cliente, id_producto, cantidad)
            )
            self.conexion.commit()
            print("Pedido insertado correctamente")
        except psycopg2.Error as e:
            self.conexion.rollback()
            print("No se pudo insertar el pedido (verifique que el cliente y producto existan):", e)

    # -- READ: listar todos los pedidos --
    def listar(self):
        self.cursor.execute(
            "SELECT id_pedido, id_cliente, id_producto, cantidad, fecha FROM pedidos ORDER BY id_pedido"
        )
        filas = self.cursor.fetchall()
        if not filas:
            print("No hay pedidos cargados")
            return
        print(f"{'ID Pedido':<12}{'ID Cliente':<12}{'ID Producto':<14}{'Cantidad':<10}{'Fecha':<12}")
        print("-" * 60)
        for f in filas:
            print(f"{str(f[0]):<12}{str(f[1]):<12}{str(f[2]):<14}{str(f[3]):<10}{str(f[4]):<12}")

    # -- UPDATE: modificar la cantidad de un pedido --
    def modificar(self, id_pedido, nueva_cantidad):
        self.cursor.execute(
            "UPDATE pedidos SET cantidad = %s WHERE id_pedido = %s",
            (nueva_cantidad, id_pedido)
        )
        self.conexion.commit()
        if self.cursor.rowcount > 0:
            print(f"Pedido actualizado ({self.cursor.rowcount} fila modificada)")
        else:
            print("No se encontro ningun pedido con ese id")

    # -- DELETE: borrar un pedido --
    def borrar(self, id_pedido):
        try:
            self.cursor.execute(
                "DELETE FROM pedidos WHERE id_pedido = %s",
                (id_pedido,)
            )
            self.conexion.commit()
            if self.cursor.rowcount > 0:
                print(f"Pedido borrado ({self.cursor.rowcount} fila eliminada)")
            else:
                print("No se encontro ningun pedido con ese id")
        except psycopg2.Error as e:
            self.conexion.rollback()
            print("No se pudo borrar el pedido:", e)

    # -- Cerrar la conexion --
    def cerrar(self):
        self.cursor.close()
        self.conexion.close()
        print("Conexion cerrada. Hasta luego!")


# ------------------------------------------------------------
#  Funcion que muestra el menu de opciones
# ------------------------------------------------------------
def mostrar_menu():
    print("\n===== GESTION DE PEDIDOS =====")
    print("1. Agregar pedido")
    print("2. Listar pedidos")
    print("3. Modificar cantidad de un pedido")
    print("4. Borrar pedido")
    print("5. Salir")
    print("==============================")


# ------------------------------------------------------------
#  Programa principal
# ------------------------------------------------------------
def main():
    # Creamos el objeto gestor (se conecta a la base)
    gestor = GestorPedidos(
        host="localhost",
        port=5432,
        dbname="comercio",
        user="postgres",
        password="IEVA"
    )

    while True:
        mostrar_menu()
        opcion = input("Elija una opcion (1-5): ")

        if opcion == "1":
            id_cliente = int(input("ID del cliente existente: "))
            id_producto = int(input("ID del producto existente: "))
            cantidad = int(input("Cantidad: "))
            gestor.crear(id_cliente, id_producto, cantidad)

        elif opcion == "2":
            gestor.listar()

        elif opcion == "3":
            id_pedido = input("Id del pedido a modificar: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            gestor.modificar(id_pedido, nueva_cantidad)

        elif opcion == "4":
            id_pedido = input("Id del pedido a borrar: ")
            gestor.borrar(id_pedido)

        elif opcion == "5":
            gestor.cerrar()
            break

        else:
            print("Opcion invalida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()