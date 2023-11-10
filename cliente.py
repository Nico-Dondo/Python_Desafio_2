# En el archivo cliente.py
import json

ARCHIVO_CLIENTES = 'clientes.json'

class Cliente:
    def __init__(self, nombre, correo, direccion, compras=None):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.compras = compras if compras is not None else []

    def comprar_producto(self, producto):
        print(f"{self.nombre} ha comprado {producto}.")
        self.compras.append(producto)

    def mostrar_compras(self):
        if self.compras:
            print(f"Compras de {self.nombre}: {', '.join(self.compras)}")
        else:
            print(f"{self.nombre} no ha realizado compras aún.")

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Dirección: {self.direccion}"

class ManejadorClientes:
    def __init__(self):
        self.clientes = self.cargar_base_datos()

    def cargar_base_datos(self):
        try:
            with open(ARCHIVO_CLIENTES, 'r') as archivo_json:
                clientes_data = json.load(archivo_json)
                return [Cliente(nombre=cliente_data['nombre'],
                                correo=cliente_data['correo'],
                                direccion=cliente_data['direccion'],
                                compras=cliente_data.get('compras', []))
                        for cliente_data in clientes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def guardar_base_datos(self):
        with open(ARCHIVO_CLIENTES, 'w') as archivo_json:
            clientes_data = [cliente.__dict__ for cliente in self.clientes]
            json.dump(clientes_data, archivo_json, indent=2)

    def registrar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        correo = input("Ingrese el correo del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")

        nuevo_cliente = Cliente(nombre, correo, direccion)
        self.clientes.append(nuevo_cliente)
        print(f"Cliente {nombre} registrado exitosamente.")

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print("\nClientes registrados:")
        for cliente in self.clientes:
            print(cliente)

    def comprar_producto(self):
        self.mostrar_clientes()
        nombre_cliente = input("Ingrese el nombre del cliente que realizará la compra: ")

        cliente_encontrado = None
        for cliente in self.clientes:
            if cliente.nombre == nombre_cliente:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            producto = input("Ingrese el nombre del producto a comprar: ")
            cliente_encontrado.comprar_producto(producto)
            print(f"Compra registrada para {cliente_encontrado.nombre}.")
        else:
            print(f"No se encontró al cliente {nombre_cliente}.")

if __name__ == "__main__":
    manejador_clientes = ManejadorClientes()

    while True:
        print("\nMENU:")
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Comprar producto")
        print("4. Guardar base de datos y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            manejador_clientes.registrar_cliente()
        elif opcion == "2":
            manejador_clientes.mostrar_clientes()
        elif opcion == "3":
            manejador_clientes.comprar_producto()
        elif opcion == "4":
            manejador_clientes.guardar_base_datos()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

