from Modelo.ProductosControl import ProductosControl

class ControlPlagas(ProductosControl):
    
    def __init__(Self, nombreProducto: str,registroIca : str, frecuencia : int,precio: float,periodoCarencia : int):
        
        super().__init__(nombreProducto,registroIca, frecuencia,precio)
        Self.__periodoCarencia = periodoCarencia
        
        
        @property
        def periodoCarencia(Self):
            return Self.__periodoCarencia
        
        @periodoCarencia.setter
        def periodoCarencia(Self, periodoCarencia):
            if periodoCarencia > 0:
                Self.__periodoCarencia = periodoCarencia
            else: 
                raise ValueError("Error en el valor del periodo de carencia")