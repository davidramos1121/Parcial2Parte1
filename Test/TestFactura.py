import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from Modelo.Facturas import Factura as factura
from Modelo.Antibioticos import Antibioticos as antibiotico
from Modelo.ControlFertilizante import ControlFertilizantes as fertilizante
from Modelo.ControlPlagas import ControlPlagas as controlPlagas
from Modelo.ProductosControl import ProductosControl as productoControl

class TestFactura(unittest.TestCase):
    
    def setUp(Self):
        
        Self.controlPlagas = controlPlagas("viruela del chiguiro", "ICA8989" , 10, 50000, 30)
        Self.fertilizante = fertilizante("vin diesel","ICA9090",20,90000,10)
        
        Self.factura = factura()
        
    
    def testVariosProductos(Self):
        Self.factura.asignarProducto(Self.controlPlagas)
        Self.factura.asignarProducto(Self.fertilizante)
        Self.assertEqual(2,len(Self.factura.productosControl), "No se encunetra el producto")
        
    
    def testVariosAntibioticos(Self):
        antibiotico_1 = antibiotico("dolexpavaca" , 3, "bovino", 300000) 
        antibiotico_2 = antibiotico("dolexpacerdo" , 90, "porcino", 900000)
        
        Self.factura.asignarAntibiotico(antibiotico_1)
        Self.factura.asignarAntibiotico(antibiotico_2)  
        
        Self.assertEqual(2,len(Self.factura.antibiotico),"No se encuentra antibiotico")
       
    def testProductoControl(Self):
        
        antibiotico_1 = antibiotico("suaviteldevaca", 5, "bovino", 300000)
        antibiotico_2 = antibiotico("suaviteldecabra", 5, "caprino", 100000)
        
        control_Plagas = controlPlagas("Covid peruano", "ICA1313", 2, 200000, 20)
        producto_fertilizante = fertilizante("Mario", "ICA1010", 10, 100000, 10)
        
        Self.factura.asignarProducto(control_Plagas)
        Self.factura.asignarProducto(producto_fertilizante)
        Self.factura.asignarAntibiotico(antibiotico_1)
        Self.factura.asignarAntibiotico(antibiotico_2)
        
        Self.assertEqual(2,len(Self.factura.antibiotico), "No se encuentra el producto")
        Self.assertEqual(2,len(Self.factura.productosControl), "No se encuentra el producto")
        
        
if __name__ == "__main__":  
    unittest.main()