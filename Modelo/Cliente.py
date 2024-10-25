class Cliente():
    
    def __init__(Self,nombre:str,cedula: str):
        Self.__nombre = nombre
        Self.__cedula = cedula
        Self.__facturas = []
        
        
    @property
    def nombre(Self):
        return Self.__nombre
    
    @nombre.setter
    def nombre(Self,nombre):
        if len (nombre) > 0:
         Self.__nombre = nombre
        else:
            raise ValueError("El campo 'nombre' no puede estar vacio")
        
    
    @property 
    def cedula(Self):
        return Self.__cedula
    
    @cedula.setter
    def cedula(Self, cedula):
        if cedula.isdigit() and len(cedula) >= 10:
            Self.__cedula = cedula
        else:
            raise ValueError("La cédula debe ser numérica y tener al menos 10 dígitos.")
        
    
    @property
    def facturas(Self):
        return Self.__facturas
    
    @facturas.setter
    def facturas(Self,facturas):
        Self.__facturas.append(facturas)