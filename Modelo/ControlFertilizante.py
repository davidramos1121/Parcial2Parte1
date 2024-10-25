from Modelo.ProductosControl import ProductosControl

class ControlFertilizantes(ProductosControl):
    
    def __init__(Self, nombreProducto:str,registroIca:str, frecuencia : int,precio:float,fechaUltimaVez : str):
        super().__init__(nombreProducto,registroIca, frecuencia,precio)
        Self.__FechaUltimaVez = fechaUltimaVez
        
    
    @property
    def fechaUltimaVez(Self):
        return Self.__FechaUltimaVez
  
    
    @fechaUltimaVez.setter
    def fechaUltimaVez(Self,fechaUltimaVez):
         if fechaUltimaVez.strip():
            Self.__FechaUltimaVez = fechaUltimaVez
         else:
            raise ValueError("Error en el valor de la fecha de la ultima aplicacion")
        