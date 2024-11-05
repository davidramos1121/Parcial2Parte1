from Modelo.ControlFertilizante import *

class CRUDFertilizante:
    def __init__(self):
        
        self.fertilizantes = []

    def agregarFertilizante(self, nombreProducto, registroIca, frecuencia, precio, fechaUltimaVez):

        fertilizante = ControlFertilizantes(nombreProducto, registroIca, frecuencia, precio, fechaUltimaVez)
        self.fertilizantes.append(fertilizante)
        print(f"Fertilizante '{nombreProducto}' agregado exitosamente.")
