import OrderDAO as o # type: ignore

def main() -> int:
    try:
        print("1. Ver todas las órdenes pendientes")
        print("2. Ver reporte de compras y ventas")
        print("3. Crear nueva orden")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            o.consultarOrdenesPendientes()

        elif opcion == 2:
            o.consultarReporteComprasVentas()

        elif opcion == 3:
            idOrden = input("Digite el ID de la orden: ")
            idCliente = input("Digite el ID del cliente: ")
            total = input("Digite el total de la orden: ")
            estado = input("Digite el estado de la orden: ")
            o.crearOrden(idOrden, idCliente, total, estado)
            print("Orden creada.")
        
        else:
            print("Opción no válida")
    except ValueError:
        print("Valores no válidos")

if __name__ == "__main__":
    main()
