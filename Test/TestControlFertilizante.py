import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from Modelo.ControlFertilizante import ControlFertilizantes

class TestControlFertilizantes(unittest.TestCase):
    
    def setUp(Self):
        Self.fertilizante = ControlFertilizantes("El matador romario", "ICA22", 15 , 300000, "2024-11-11")
        
    
    def test_control_fertilizante(Self):
        
        Self.assertEqual(Self.fertilizante.nombreProducto, "El matador romario")
        Self.assertEqual(Self.fertilizante.registroIca, "ICA22")
        Self.assertEqual(Self.fertilizante.frecuencia, 15)
        Self.assertEqual(Self.fertilizante.precio, 300000)
        Self.assertEqual(Self.fertilizante.fechaUltimaVez, "2024-11-11")
        
    
    def test_registro_ica_vacio(Self):
        
        with Self.assertRaises(ValueError) as context:
            Self.fertilizante.registroIca = ""
        Self.assertEqual(str(context.exception), "El registro ICA no puede estar vacio")
        
        
    def test_fecha_invalida(Self):
        
        with Self.assertRaises(ValueError) as context:
            Self.fertilizante.fechaUltimaVez = ""
        Self.assertEqual(str(context.exception), "Error en la fecha de la ultima vez")


if __name__ == '__main__':
    unittest.main()