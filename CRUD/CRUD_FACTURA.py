# CRUD/CRUDFactura.py
class CRUDFactura:
    def __init__(self):
        self.facturas = []  

    def agregarFactura(self, factura):
        self.facturas.append(factura)
        print("Factura agregada exitosamente.")

    def buscarFactura(self, numero_factura):
        for factura in self.facturas:
            if factura.numero == numero_factura:  
                return factura
        print("Factura no encontrada.")
        return None

    def listarFacturas(self):
        if not self.facturas:
            print("No hay facturas registradas.")
        else:
            for factura in self.facturas:
                print(f"Factura #{factura.numero}, Cliente: {factura.cliente.nombre}")

    def eliminarFactura(self, numero_factura):
        factura = self.buscarFactura(numero_factura)
        if factura:
            self.facturas.remove(factura)
            print(f"Factura #{numero_factura} eliminada exitosamente.")
