#Importación del módulo unittest para realizar pruebas unitarias
import unittest
#Importación de la clase Calculadora desde el archivo calculadora.py
from calculadora import Calculadora

#Prueba del método resta
class TestCalculadora(unittest.TestCase):

    #Prueba la resta de dos números positivos
    def test_resta_positivos(self):
        self.assertEqual(Calculadora.resta(2, 1), 1)

    #Prueba la resta de dos números iguales (debe dar cero)
    def test_resta_iguales(self):
        self.assertEqual(Calculadora.resta(2, 2), 0)


#Prueba del método multiplicación
#Prueba la multiplicación de dos números positivos
    def test_multiplicacion_positivos(self):
        self.assertEqual(Calculadora.multiplicacion(2, 3), 6)

#Prueba la multiplicación por cero (debe dar cero)
    def test_multiplicacion_cero(self):
        self.assertEqual(Calculadora.multiplicacion(2, 0), 0)

#Prueba la multiplicación de un número negativo por uno positivo
    def test_multiplicacion_negativo_positivo(self):
        self.assertEqual(Calculadora.multiplicacion(-2, 3), -6)


#Prueba del método división
#Prueba la división exacta
    def test_division_exacta(self):
        self.assertEqual(Calculadora.division(6, 3), 2)

#Prueba la división con resultado decimal
    def test_division_decimal(self):
        self.assertEqual(Calculadora.division(5, 2), 2.5)

#Prueba la división periódica usando assertAlmostEqual para comparar con precisión limitada
    def test_division_periodica(self):
        self.assertAlmostEqual(Calculadora.division(1, 3), 0.3333333333333333, places=10)

#Bloque condiciomal que permite ejecutar las pruebas directamente
if __name__ == "__main__":
    #Inicializar la ejecución de todas las pruebas definidas em la clase 
    unittest.main()