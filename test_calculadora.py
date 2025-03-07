#Importacon del modulo a testear
import unittest
#Importacion de la clase calculadora
from calculadora import Calculadora

#Definicion de la clase TestCalculadora
class TestCalculadora(unittest.TestCase):
    #Metodo que se ejecuta antes de  cada prueba
    def setUp(self):
          self.calculadora = Calculadora()
    #Prueba del metodo suma
    def test_suma(self):
        #Pruba la suma de dos numeros ppositivos
        self.assertEqual(self.calculadora.suma(5, 2), 7)
        #Prueba la suma de dos numeros ceros
        self.assertEqual(self.calculadora.suma(0, 0), 0)
        
    #Metodo de prueba para el metodo resta
    def test_resta(self):
        #Prueba la resta de dos numeros positivos
        self.assertEqual(self.calculadora.resta(5, 2), 3)
        #Prueba la resta de dos numeros iguales
        self.assertEqual(self.calculadora.resta(3, 3), 0)   
        
    #Metodo de prueba para el metodo multiplicacion
    def test_multiplicacion(self):
        #Prueba la multiplicacion de dos numeros positivos
        self.assertEqual(self.calculadora.multiplicacion(5, 2), 10)
        #Prueba la multiplicacion por ceros(debe dar ceros)
        self.assertEqual(self.calculadora.multiplicacion(5, 0), 0)
        #Prueba de la multipliacio de un numero  negaticop por un positivo
        self.assertEqual(self.calculadora.multiplicacion(-5, 2), -10)
        
    #Metodo de prueba para el metodo division
    def test_division(self):
        #Prueba la division exacta
        self.assertEqual(self.calculadora.division(6, 2), 3)
        #Prueba la division  co el mresultado decimal
        self.assertEqual(self.calculadora.division(5, 2), 2.5)
        #Prueba la division periodica usando assertAlmostEqual para comparar con presicion limitada
        self.assertAlmostEqual(self.calculadora.division(1, 3), 0.3333333333333333)
    
if __name__ == '__main__':
    unittest.main()
