from unittest import TestCase
from dzien10.czekolada import Czekolada
from tools.catch_print import *

class CzekoTesty(TestCase):

    def test_podaj_producenta(self):
        czekolada = Czekolada('mleczna', 'wedel', 150)
        oczekiwany_prod = 'wedel\n'

        rzeczywisty_prod = get_print_output(czekolada.podaj_producenta)

        self.assertEqual(rzeczywisty_prod, oczekiwany_prod)