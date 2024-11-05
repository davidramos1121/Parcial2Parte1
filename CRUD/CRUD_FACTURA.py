class CRUDFactura:
    def __init__(self):
        self.facturas = []  
        self.numero_factura = 1  

    def agregarFactura(self, factura):
        factura.numero = self.numero_factura  
        self.facturas.append(factura)
        self.numero_factura += 1  
        print("Factura agregada exitosamente.")

    def buscarFactura(self, numero_factura):
        for factura in self.facturas:
            if factura.numero == numero_factura:
                return factura
        print("Factura no encontrada.")
        return None

    def listarFacturas(self, cliente):
        facturas_cliente = [factura for factura in self.facturas if factura.cliente.cedula == cliente.cedula]
        if not facturas_cliente:
            print("No hay facturas registradas para este cliente.")
        else:
            print(f"Facturas para el cliente {cliente.nombre}:")
            for factura in facturas_cliente:
                print(f"Factura #{factura.numero}, Fecha: {factura.fecha} (total: {factura.calcularTotal()})") 
