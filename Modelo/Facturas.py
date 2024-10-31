class Factura(): 
    
    def __init__(Self):
           
        Self.__antibiotico = []        
        Self.__productoControl = []   


    @property
    def antibiotico(Self):
        return Self.__antibiotico
    
    @antibiotico.setter
    def antibiotico(Self, antibiotico):
        Self.__antibiotico.append(antibiotico)


    @property
    def productosControl(Self):
        return Self.__productoControl
    
    @productosControl.setter
    def productosControl(Self, productoControl):
        Self.__productoControl.append(productoControl)
        

    def asignarProducto(Self, productoControl):
        Self.productoControl = productoControl
        

    def asignarAntibiotico(Self, antibiotico):
        Self.antibiotico = antibiotico


    def compra(Self, producto=None, antibiotico=None):
        if producto is not None:
            Self.asignarProducto(producto)
        if antibiotico is not None:
            Self.asignarAntibiotico(antibiotico)

