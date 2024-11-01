from Modelo.ProductosControl import ProductosControl

class CRUDProducto:
    def __init__(self):
        self.productos = [] 

    def agregarProducto(self, nombreProducto, registroIca, frecuencia, precio):
        nuevo_producto = ProductosControl(nombreProducto, registroIca, frecuencia, precio)
        self.productos.append(nuevo_producto)
        print(f"Producto '{nuevo_producto.nombreProducto}' agregado exitosamente.")