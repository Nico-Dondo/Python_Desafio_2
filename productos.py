import json

ARCHIVO_PRODUCTOS = 'productos.json'

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Producto: {self.nombre}"

    def to_dict(self):
        return {"nombre": self.nombre}

class ManejadorProductos:
    def __init__(self):
        self.base_de_datos = self.cargar_base_datos()

    def cargar_base_datos(self):
        productos_predefinidos = ["TV", "Heladera", "Celular", "Playstation"]
        return {producto: Producto(producto) for producto in productos_predefinidos}

    def guardar_base_datos(self):
        with open(ARCHIVO_PRODUCTOS, 'w') as archivo_json:
            productos_data = [producto.to_dict() for producto in self.base_de_datos.values()]
            json.dump(productos_data, archivo_json, indent=2)

    def mostrar_productos(self):
        if not self.base_de_datos:
            print("No hay productos registrados.")
            return []

        print("\nProductos registrados:")
        productos = list(self.base_de_datos.values())
        for producto in productos:
            print(producto)
        return productos

    def agregar_producto(self, producto):
        self.base_de_datos[producto.nombre] = producto
        print(f"Producto '{producto.nombre}' agregado exitosamente.")
