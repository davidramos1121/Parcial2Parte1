import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modelo.Cliente import Cliente as cliente
from Modelo.Facturas import Factura as factura
from Modelo.Antibioticos import Antibioticos as antibiotico 
from Modelo.ControlFertilizante import ControlFertilizantes as fertilizante
from Modelo.ControlPlagas import ControlPlagas as controlPlagas

class TestCliente(unittest.TestCase):
    
 def setUp(Self):  
     
        Self.factura_1 = factura()
        Self.factura_2 = factura()

        Self.cliente = cliente("Sting", "1010101010")
        Self.antibiotico_1 = antibiotico("anticoprofago", "5", "bovino", 120000)
        Self.antibiotico_2 = antibiotico("vilkbrino", "15", "caprino", 100000)
        Self.antibiotico_3 = antibiotico("copig", "15", "porcino", 300000)
        Self.controlPlagas = controlPlagas("viruela del mono promax", "ICA1313", 7, 30000, 20)
        Self.fertilizante = fertilizante("LaGrin", "ICA4", 7, 90000, 8)


 def testVariasFacturas(Self):
     
     Self.factura_1.asignarAntibiotico(Self.antibiotico_1)
     Self.factura_1.asignarAntibiotico(Self.antibiotico_2)
     Self.factura_1.asignarAntibiotico(Self.antibiotico_3)
     Self.factura_1.asignarProducto(Self.controlPlagas)
     Self.factura_1.asignarProducto(Self.fertilizante)
     
     Self.factura_2.asignarAntibiotico(Self.antibiotico_1)
     Self.factura_2.asignarAntibiotico(Self.antibiotico_2)
     Self.factura_2.asignarAntibiotico(Self.antibiotico_3)
     Self.factura_2.asignarProducto(Self.controlPlagas)
     Self.factura_2.asignarProducto(Self.fertilizante)
     
     Self.cliente.facturas.append(Self.factura_1)
     Self.cliente.facturas.append(Self.factura_2)
     
     Self.assertEqual(2, len(Self.cliente.facturas), "El cliente no tiene facturas previas")
     
  
def testSinFacturas(Self): 
     
     Self.assertEqual(2, len(Self.cliente.facturas), "El cliente no tiene facturas")
     
     
     
     
if __name__ == "__main__":  
    unittest.main() 
    