import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from Modelo.ControlPlagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):
    
    def setUp(Self):        
        Self.controlPlaga = ControlPlagas("PlagassinRodeos", "ICA123", 20, 100000, 2)

    def testRegistroCorrecto(Self):
        Self.assertEqual(Self.controlPlaga.registroIca, "ICA123")
        Self.assertEqual(Self.controlPlaga.nombreProducto, "PlagassinRodeos")
        Self.assertEqual(Self.controlPlaga.frecuencia, 20)
        Self.assertEqual(Self.controlPlaga.precio, 100000)
        Self.assertEqual(Self.controlPlaga.periodoCarencia, 2)

    def testPeriodoCarencia(Self):
        with Self.assertRaises(ValueError) as context:
            Self.controlPlaga.periodoCarencia = -10
        Self.assertEqual(str(context.exception), "Error en el valor del periodo de carencia")
            
if __name__ == "__main__":
    unittest.main()
