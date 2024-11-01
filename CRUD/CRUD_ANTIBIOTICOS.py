from Modelo.Antibioticos import Antibioticos

class CRUDAntibioticos:
    
    def __init__(Self):
        Self.Antibioticos = [] 

    def agregarAntibioticos(Self,nombre,dosis,tipoAnimal,precio):
        nuevo_antibiotico = Antibioticos(nombre, dosis, tipoAnimal, precio)
        Self.antibiotico.append(nuevo_antibiotico)
        print(f"Antibiotico '{nuevo_antibiotico.nombre}' agregado exitosamente.")