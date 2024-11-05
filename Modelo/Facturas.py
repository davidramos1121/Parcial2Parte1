
class Factura:
    def __init__(self,cliente):
        self.cliente = cliente
        self.__antibioticos = []       
        self.__productosControl = []  
        self.numero = None    

    @property
    def antibioticos(self):
        return self.__antibioticos
    
    @property
    def productosControl(self):
        return self.__productosControl

    def asignarProducto(self, productoControl):
        self.__productosControl.append(productoControl)  

    def asignarAntibiotico(self, antibiotico):
        self.__antibioticos.append(antibiotico)  

    def imprimirFactura(self):
        print("\nFactura Detallada:")
        print("Antibióticos comprados:", [antibiotico for antibiotico in self.__antibioticos])
        print("Productos de control comprados:", [producto for producto in self.__productosControl])
        print("")
