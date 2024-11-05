from Modelo.Cliente import Cliente
from Modelo.Facturas import Factura
from CRUD.CRUD_FACTURA import CRUDFactura

class CRUDCliente:
    def __init__(self, crud_factura):
        self.clientes = []
        self.crud_factura = crud_factura
    

    def agregarCliente(self, nombre, cedula):
        cliente = Cliente(nombre, cedula)
        self.clientes.append(cliente)
        print(f"Cliente '{nombre}' agregado exitosamente.")

    def buscarCliente(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def buscar_por_cedula(self, cedula):
        cliente = self.buscarCliente(cedula)
        if cliente:
            print(f"Cliente: {cliente.nombre} (Cédula: {cliente.cedula})")
            if cliente.facturas:
                print("Facturas asociadas:")
                for factura in cliente.facturas:
                    print(f"Factura para {factura.cliente.nombre}")  
                    factura.imprimirFactura()  
            else:
                print("No hay facturas asociadas con este cliente.")
        else:
            print("Cliente no encontrado.")

    def venderProducto(self, cedula, productos, antibioticos):
     cliente = self.buscarCliente(cedula)
     if cliente:
        factura = Factura(cliente)  
        for producto in productos:
            factura.asignarProducto(producto)
        for antibiotico in antibioticos:
            factura.asignarAntibiotico(antibiotico)

        cliente.facturas.append(factura)  
        self.crud_factura.agregarFactura(factura)
        print("Factura agregada exitosamente.")
        return factura
     else:
        print("Cliente no encontrado, no se pudo generar la factura.")
        return None


    def listarClientes(self):
        if self.clientes:
            print("Lista de Clientes:")
            for cliente in self.clientes:
                print(f"{cliente.nombre} (Cédula: {cliente.cedula})")
        else:
            print("No hay clientes registrados.")
