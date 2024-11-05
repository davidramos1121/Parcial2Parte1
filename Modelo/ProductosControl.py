class ProductosControl():
    
    def __init__(Self, nombreProducto,registroIca, frecuencia,precio):
        Self.__nombreProducto =  nombreProducto
        Self.__registroIca = registroIca
        Self.__frecuencia = frecuencia
        Self.__precio = precio
        
        
    @property
    def nombreProducto(Self):
        return Self.__nombreProducto
    
    @nombreProducto.setter
    def nombreProducto(Self,nombreProducto):
         if not nombreProducto.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        
         Self.__nombreProducto = nombreProducto
        
    
    @property
    def registroIca(Self):
        return Self.__registroIca
    
    @registroIca.setter 
    def registroIca(Self, registroIca):
        if len(registroIca.strip()) > 0:
            Self.__registroIca = registroIca
        else:
            raise ValueError("El registro ICA no puede estar vacio.")
        
    
    @property
    def frecuencia(Self):
        return Self.__frecuencia
    
    @frecuencia.setter
    def frecuencia(Self, frecuencia):
        if frecuencia > 0:
            Self.__frecuencia = frecuencia
        else: 
            raise ValueError("Error en el valor de la frecuencia de aplicacion")
        
  
    @property 
    def precio(Self):
        return Self.__precio
    
    @precio.setter
    def precio(Self,precio):
        if precio > 0:
            Self.__precio = precio
        else: 
            raise ValueError("Error en el precio del producto") 
        