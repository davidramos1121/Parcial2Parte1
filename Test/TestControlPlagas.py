import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from Modelo.ControlPlagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):
    
    def setUp(Self):        
        Self.controlPlaga = ControlPlagas("ICA123" , "PlagasinRodeos",20,100000,2)

        
    def TestValido(Self):
        
        Self.assertEqual(Self.controlPlaga.registroIca,"ICA123")
        Self.assertEqual(Self.controlPlaga.nombreProducto,"PlagassinRodeos")
        Self.assertEqual(Self.controlPlaga.frecuencia, 20)
        Self.assertEqual(Self.controlPlaga.precio, 100000)
        Self.assertEqual(Self.controlPlaga.periodoCarencia,2)
        
        