from Modelo.ControlPlagas import *

class CRUDControlPlagas:
    
    def __init__(Self):
        Self.controlPlagas = [] 

    def agregarProductoControlPlagas(Self,nombreProducto,registroIca, frecuencia ,precio,periodoCarencia):
        nuevo_controlPlagas = ControlPlagas(nombreProducto, registroIca, frecuencia, precio,periodoCarencia)
        Self.controlPlagas.append(nuevo_controlPlagas)
        print(f"Producto '{nuevo_controlPlagas.nombreProducto}' agregado exitosamente.")