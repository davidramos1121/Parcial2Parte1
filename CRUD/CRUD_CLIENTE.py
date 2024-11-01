from Modelo.Cliente import Cliente
from Modelo.Facturas import Factura

class CRUDCliente:
    
    def __init__(Self):
        Self.clientes= []
        
    def agregarCliente(Self,nombre,cedula):
        
        nuevoCliente = Cliente(nombre, cedula)
        Self.clientes.append(nuevoCliente)
        return nuevoCliente
    
    def buscarCliente(Self, cedula):

        for cliente in Self.clientes:
            if cliente.cedula == cedula:
                return cliente 
        return None
    
    def venderProducto(Self, cedula, productos=None, antibioticos=None):
        
        cliente = Self.buscarCliente(cedula)
        if cliente:
            factura = Factura()

            if productos:
                for producto in productos:
                    factura.asignarProducto(producto)
  
            if antibioticos:
                for antibiotico in antibioticos:
                    factura.asignarAntibiotico(antibiotico)

            print(f"Factura generada para el cliente {cliente.nombre} (Cedula: {cliente.cedula}):")
            print("Antibioticos comprados:", factura.antibiotico)
            print("Productos de control comprados:", factura.productosControl)
            return factura
        else:
            print("Cliente no encontrado.")
            return None