from unittest import TestCase
from dzien12.kalkulator import *

class KalkulatorTesty(TestCase):
    def setUp(self):
        self.a = 2
        self.b = 3

    def test_dodaj(self):
        # arrange
        wynik_oczekiwany = self.a + self.b

        # act
        wynik_rzeczywisty = dodaj(self.a, self.b)

        # assert
        self.assertEqual(wynik_rzeczywisty, wynik_oczekiwany, 'Wartości obliczone są różne.')

    def test_odejmij(self):
        # arrange
        wynik_oczekiwany = self.b - self.a

        # act
        wynik_rzeczywisty = odejmij(self.a, self.b)

        # assert
        self.assertEqual(wynik_rzeczywisty, wynik_oczekiwany)

    def test_pomnoz(self):
        # arrange
        wynik_oczekiwany = self.a * self.b

        # act
        wynik_rzeczywisty = pomnoz(self.a, self.b)

        # assert
        self.assertEqual(wynik_rzeczywisty, wynik_oczekiwany)
