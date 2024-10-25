import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from Modelo.Antibioticos import *

class TestAntibioticos(unittest.TestCase):
    
    def setUp(Self):
        Self.antibiotico = Antibioticos ("penicilina", 400, "caprino", 30000)
        

    def test_antibioticos(Self):
        
        Self.assertEqual(Self.antibiotico.nombre, "penicilina")
        Self.assertEqual(Self.antibiotico.dosis, 400)
        Self.assertEqual(Self.antibiotico.tipoAnimal, "caprino")
        Self.assertEqual(Self.antibiotico.precio, 30000)
        
        
    def test_animal_incorrecto(Self):
        
        with Self.assertRaises(ValueError) as context:
            Self.antibiotico.tipoAnimal = "perro"
        Self.assertEqual(str(context.exception), "El tipo de animal debe ser 'bovino', 'caprino' o 'porcino'")
        
        
        
    def test_dosis_incorrecta(Self):
        
        with Self.assertRaises(ValueError) as context:
           Self.antibiotico.dosis = 150
        Self.assertEqual(str(context.exception), "La dosis debe estar entre 400 kg y 600 kg")
        
        

if __name__ == '__main__':
    unittest.main()