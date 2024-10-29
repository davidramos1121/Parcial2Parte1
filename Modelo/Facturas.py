class Factura(): 
    
    def __init__(Self):
           
        Self.__antibiotico = []        
        Self.__producto = []   


    @property
    def antibiotico(Self):
        return Self.__antibiotico
    
    @antibiotico.setter
    def antibiotico(Self, antibiotico):
        Self.__antibiotico.append(antibiotico)


    @property
    def productosControl(Self):
        return Self.__producto_control
    
    @productosControl.setter
    def producto_control(Self, producto):
        Self.__producto.append(producto)
        

    def asignarProducto(Self, producto):
        Self.producto = producto
        

    def asignarAntibiotico(Self, antibiotico):
        Self.antibiotico = antibiotico


    def compra(Self, producto=None, antibiotico=None):
        if producto is not None:
            Self.asignarProducto(producto)
        if antibiotico is not None:
            Self.asignarAntibiotico(antibiotico)

