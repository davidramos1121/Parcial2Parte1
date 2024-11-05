from Modelo.Cliente import Cliente
from Modelo.Facturas import Factura

class CRUDCliente:
    
    def __init__(self):
        self.clientes = []  
   
        
    def agregarCliente(self, nombre, cedula):
        nuevoCliente = Cliente(nombre, cedula)  
        self.clientes.append(nuevoCliente)  
        return nuevoCliente
  
    
    def buscarCliente(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente  
        return None  
  
    
    def venderProducto(self, cedula, productos=None, antibioticos=None):
        cliente = self.buscarCliente(cedula)
        if cliente:
            factura = Factura()
            if productos:
                for producto in productos:
                    factura.asignarProducto(producto)  
            else:
                print("No se vendieron productos.")
            if antibioticos:
                for antibiotico in antibioticos:
                    factura.asignarAntibiotico(antibiotico) 
            else:
                print("No se vendieron antibioticos.")
            cliente.facturas.append(factura)
            print(f"Factura generada para el cliente {cliente.nombre} (Cedula: {cliente.cedula}):")
            print("")
            factura.imprimirFactura() 
            return factura  
        else:
            print("No se pudo realizar la venta. Cliente no encontrado.")
            return None
 
    
    def buscar_por_cedula(self, cedula):
        cliente = self.buscarCliente(cedula)
        if cliente:
            print(f"Cliente: {cliente.nombre} (Cedula: {cliente.cedula})")
            if cliente.facturas:
                print("Facturas asociadas:")
                for i, factura in enumerate(cliente.facturas):
                    print(f"\nFactura #{i + 1}")
                    factura.imprimirFactura()  
            else:
                print("No hay facturas asociadas con este cliente.")
        else:
            print("Cliente no encontrado.")
