class ProductosControl():
    
    def __init__(Self, nombre, frecuencia,precio):
        Self.Nombre =  nombre
        Self.Frecuencia = frecuencia
        Self.Precio = precio
        

class ControlPlagas(ProductosControl):
    
    def __init__(Self,periodoCarencia):
        Self.PeriodoCarencia = periodoCarencia

print("hoal")
class ControlFertilizantes(ProductosControl):
    
    def __init__(Self,fechaUltimaVez):
        Self.FechaUltimaVez = fechaUltimaVez
        

class Antibioticos ():
    
    def __init__(Self, nombre, dosis, tipoAnimal ,precio):
        Self.Nombre = nombre
        Self.Dosis = dosis
        Self.TipoAnimal = tipoAnimal
        Self.Precio = precio
        
        
class Cliente():
    
    def __init__(self,nombre,cedula):
        self.Nombre = nombre
        self.Cedula = cedula
        

class Factura(): 
    
    def __init__(self,fecha,costo):
        self.Fecha = fecha
        self.Costo = costo
        

        
            