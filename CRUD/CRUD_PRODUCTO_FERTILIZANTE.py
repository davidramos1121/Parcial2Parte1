from Modelo.ControlFertilizante import *

class CRUDFertilizante:
    def __init__(self):
        
        self.fertilizantes = []

    def agregarFertilizante(self, nombreProducto, registroIca, frecuencia, precio, fechaUltimaVez):

        fertilizante = ControlFertilizantes(nombreProducto, registroIca, frecuencia, precio, fechaUltimaVez)
        self.fertilizantes.append(fertilizante)
        print(f"Fertilizante '{nombreProducto}' agregado exitosamente.")

""" 
    def listarFertilizantes(self):
 
        if not self.fertilizantes:
            print("No hay fertilizantes registrados.")
            return []
        
        print("Lista de fertilizantes disponibles:")
        for idx, fertilizante in enumerate(self.fertilizantes, start=1):
            print(f"{idx}. {fertilizante.nombreProducto} - Registro ICA: {fertilizante.registroIca} - Frecuencia: {fertilizante.frecuencia} días - Precio: ${fertilizante.precio} - Última aplicación: {fertilizante.fechaUltimaVez}")
        return self.fertilizantes

    def buscarFertilizante(self, nombreProducto):
     
        for fertilizante in self.fertilizantes:
            if fertilizante.nombreProducto.lower() == nombreProducto.lower():
                print(f"Fertilizante encontrado: {fertilizante.nombreProducto} - Registro ICA: {fertilizante.registroIca} - Frecuencia: {fertilizante.frecuencia} días - Precio: ${fertilizante.precio} - Última aplicación: {fertilizante.fechaUltimaVez}")
                return fertilizante
        print(f"No se encontró el fertilizante con nombre '{nombreProducto}'.")
        return None

    def eliminarFertilizante(self, nombreProducto):
        
        for fertilizante in self.fertilizantes:
            if fertilizante.nombreProducto.lower() == nombreProducto.lower():
                self.fertilizantes.remove(fertilizante)
                print(f"Fertilizante '{nombreProducto}' eliminado exitosamente.")
                return True
        print(f"No se encontró el fertilizante con nombre '{nombreProducto}' para eliminar.")
        return False
"""