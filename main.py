# Archivo: main.py

from cliente import Cliente, ManejadorClientes
from productos import ManejadorProductos


def main():
    manejador_clientes = ManejadorClientes()
    manejador_productos = ManejadorProductos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            manejador_clientes.registrar_cliente()
        elif opcion == "2":
            manejador_clientes.mostrar_clientes()
        elif opcion == "3":
            manejador_productos.mostrar_productos()
        elif opcion == "4":
            manejador_clientes.comprar_producto()
        elif opcion == "5":
            manejador_clientes.guardar_base_datos()
            manejador_productos.guardar_base_datos()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

def mostrar_menu():
    print("\nMENU:")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Mostrar productos")
    print("4. Comprar producto")
    print("5. Salir del programa")

if __name__ == "__main__":
    main()
