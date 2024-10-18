import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modelo.Modelo import *
import unittest

class TestProductosControl(unittest.TestCase):
    
    def test_productos_control(Self):
         
        producto = ProductosControl("insecticida", 4 , 3000)
        
        Self.assertEqual(producto.Nombre, "insecticida")
        Self.assertEqual(producto.Frecuencia, 4)
        Self.assertEqual(producto.Precio, 3000)
        
        
class TestControlPlagas(unittest.TestCase):
    
    def test_control_plagas(Self):
        
        control_plagas = ControlPlagas(15)
        
        Self.assertEquals(control_plagas.PeriodoCarencia, 15)
        

class TestControlFertilizantes(unittest.TestCase):
    
    def test_control_fertilizante(Self):
        
        fertilizante = ControlFertilizantes("2024-11-21")
        
        Self.assertEqual(fertilizante.FechaUltimaVez, "2024-11-21")
        
        
class TestAntibioticos(unittest.TestCase):

    def test_antibioticos(Self):
  
        antibiotico = Antibioticos("Penicilina", "500mg", "Vaca", 10.5)
        
        Self.assertEqual(antibiotico.Nombre, "Penicilina")
        Self.assertEqual(antibiotico.Dosis, "500mg")
        Self.assertEqual(antibiotico.TipoAnimal, "Vaca")
        Self.assertEqual(antibiotico.Precio, 10.5)
        

class TestCliente(unittest.TestCase):

    def test_cliente(Self):

        cliente = Cliente("Juan", "12345678")
  
        Self.assertEqual(cliente.Nombre, "Juan")
        Self.assertEqual(cliente.Cedula, "12345678")
        

class TestFactura(unittest.TestCase):

    def test_factura(Self):

        factura = Factura("2024-10-16", 100.0)
 
        Self.assertEqual(factura.Fecha, "2024-10-16")
        Self.assertEqual(factura.Costo, 100.0)
        
if __name__ == '__main__':
    unittest.main()