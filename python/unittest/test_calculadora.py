import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_sumar(self):
        resultado = self.calculadora.sumar(3, 2)
        self.assertEqual(resultado, 5)

    def test_restar(self):
        resultado = self.calculadora.restar(5, 2)
        self.assertEqual(resultado, 3)

    def test_multiplicar(self):
        resultado = self.calculadora.multiplicar(4, 3)
        self.assertEqual(resultado, 12)

    def test_dividir(self):
        resultado = self.calculadora.dividir(6, 2)
        self.assertEqual(resultado, 3)

if __name__ == '__main__':
    unittest.main()
