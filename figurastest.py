import unittest
from figuras import Figuras


class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.figuras = Figuras()

    def test_area_cuadrado_lado_5(self):

        resultado = self.figuras.cuadrado(5)
        self.assertEqual(25, resultado)

    def test_area_cuadrado_lado_6(self):

        resultado = self.figuras.cuadrado(6)
        self.assertEqual(36, resultado)

    def test_area_cuadrado_lado_7(self):

        resultado = self.figuras.cuadrado(7)
        self.assertEqual(41, resultado)

    def test_area_cuadrado_lado_g(self):

        resultado = self.figuras.cuadrado('g')
        self.assertEqual('dato incorrecto', resultado)

    def test_area_cuadrado_lado_4_punto_5(self):

        resultado = self.figuras.cuadrado(4.5)
        self.assertEqual(20.25, resultado)

    def test_area_rectangulo_base_5_altura_4(self):

        resultado = self.figuras.rectangulo(5, 4)
        self.assertEqual(20, resultado)

    def test_area_rectangulo_base_7_altura_3(self):

        resultado = self.figuras.rectangulo(7, 3)
        self.assertEqual(21, resultado)

    def test_area_rectangulo_base_5_3_altura_4_2(self):

        resultado = self.figuras.rectangulo(5.3, 4.2)
        self.assertEqual(22.26, resultado)

    def test_area_rectangulo_base_gg(self):

        resultado = self.figuras.rectangulo('gg', 'izi')
        self.assertEqual('dato incorrecto', resultado)

    def test_area_triangulo_base_5_altura_4(self):

        resultado = self.figuras.triangulo(5, 4)
        self.assertEqual(10, resultado)

    def test_area_triangulo_base_izi_gg(self):

        resultado = self.figuras.triangulo('izi', 'gg')
        self.assertEqual('dato incorrecto', resultado)

    def test_area_circulo_base_8(self):

        resultado = self.figuras.circulo(8)
        self.assertEqual(201.0624, resultado)

    def test_area_circulo_base_izi_gg_circulo(self):

        resultado = self.figuras.circulo('circulo')
        self.assertEqual('dato incorrecto', resultado)

if __name__ == '__main__':
    unittest.main()
