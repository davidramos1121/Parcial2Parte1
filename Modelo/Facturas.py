class Factura(): 
    
    def __init__(Self,fecha : str,costo : float):
        Self.__fecha = fecha
        Self.__costo = costo
        
    
    @property
    def fecha(Self):
        return Self.__fecha
    
    @fecha.setter
    def fecha(Self, fecha):
        if fecha.strip():
            Self.__fecha = fecha
        else:
            raise ValueError("Error en la fecha de la factura")
        
        
    @property
    def costo(Self):
        return Self.__costo
    
    @fecha.setter
    def costo(Self, costo):
        if costo.strip():
            Self.__fecha = costo
        else:
            raise ValueError("Error en la digitacion del costo")
        
