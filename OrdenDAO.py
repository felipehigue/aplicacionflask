import mysql.connector

# Función para la conexión
def getConnection():
    conn = None
    try:
        conn = mysql.connector.connect(user="root", password="Lun14140027*", host="127.0.0.1", database="desarrollo", port="3306")
    except:
        print("No se puede conectar a la base de datos")
        return 0
    print("Conectado")
    return conn

# Función para cerrar la conexión
def unconnection(conn):
    conn.close()

# Consultar órdenes pendientes
def consultarOrdenesPendientes():
    conn = getConnection()
    c = conn.cursor()

    query = """SELECT * FROM ordenes WHERE estado = 'pendiente'"""
    c.execute(query)

    ordenesPendientes = c.fetchall()

    for orden in ordenesPendientes:
        print(orden)

    unconnection(conn)

# Consultar reportes de compras y ventas
def consultarReporteComprasVentas():
    conn = getConnection()
    c = conn.cursor()

    queryCompras = """SELECT * FROM compras"""
    queryVentas = """SELECT * FROM ventas"""

    print("Reporte de Compras:")
    c.execute(queryCompras)
    compras = c.fetchall()
    for compra in compras:
        print(compra)

    print("\nReporte de Ventas:")
    c.execute(queryVentas)
    ventas = c.fetchall()
    for venta in ventas:
        print(venta)

    unconnection(conn)

# Crear nueva orden (insertar)
def crearOrden(idOrden, idCliente, total, estado):
    conn = getConnection()
    c = conn.cursor()
    ordenInsert = """INSERT INTO ordenes (idOrden, idCliente, total, estado) VALUES (%s, %s, %s, %s)"""
    val = (idOrden, idCliente, total, estado)
    c.execute(ordenInsert, val)
    conn.commit()
    print(c.rowcount, "orden insertada.")
    unconnection(conn)

# Añadir un bloque principal para ejecutar las funciones
def main():
    # Llamar a la función que desees probar
    print("Consultando órdenes pendientes:")
    consultarOrdenesPendientes()

    print("\nConsultando reporte de compras y ventas:")
    consultarReporteComprasVentas()

    print("\nInsertando nueva orden:")
    crearOrden(7, 7, 560.00, 'pendiente')

# Si el archivo se ejecuta directamente, llama a la función main
if __name__ == "__main__":
    main()
