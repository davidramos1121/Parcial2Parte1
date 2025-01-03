class Antibioticos ():
    
    def __init__(Self, nombre: str, dosis : float, tipoAnimal: str,precio : float):
        Self.__nombre = nombre
        Self.__dosis = dosis
        Self.__tipoAnimal = tipoAnimal
        Self.__precio = precio
        
        
    @property
    def nombre(Self):
        return Self.__nombre
     
    @nombre.setter
    def nombre(Self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre del antibiotico no puede estar vacio.")
        if not all(char.isalpha() or char.isspace() for char in nombre):
            raise ValueError("El nombre del antibiotico solo puede contener letras y espacios.")
        Self.__nombre = nombre
        
    
    @property
    def dosis(Self):
        return Self.__dosis
    
    @dosis.setter
    def dosis(Self, dosis):
        if 400 <= dosis <= 600:
            Self.__dosis = dosis
        else:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")
        
        
    @property
    def tipoAnimal(Self):
        return Self.__tipoAnimal
    
    @tipoAnimal.setter
    def tipoAnimal(Self, tipoAnimal):
        if tipoAnimal.lower() in ['bovino', 'caprino', 'porcino']:
            Self.__tipoAnimal = tipoAnimal
        else:
            raise ValueError("El tipo de animal debe ser 'bovino', 'caprino' o 'porcino'.")
        
    
    @property
    def precio(Self):
        return Self.__precio
    
    @precio.setter
    def precio(Self,precio):
        if precio > 0:
            Self.__precio = precio
        else: 
            raise ValueError("Error en el precio del producto") 
        