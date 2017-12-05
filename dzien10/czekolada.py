from dzien10.producent import Producent

class Czekolada(object):
    def __init__(self, rodzaj, producent, waga, nadzienie=None):
        self.rodzaj = rodzaj
        self.producent = producent
        self.waga = waga
        self.cena = None
        self.nadzienie = nadzienie

    def __str__(self):
        return f'Czekolada {self.rodzaj} od {self.producent.nazwa}'

    def zjedz(self, ilosc_g):
        if self.waga - ilosc_g  <= 0:
            print('Nie ma aż tyle czekolady, łasuchu.')
        else:
            self.waga -= ilosc_g
            print('Bon apetit!')

    def __add__(self, other):
        return self.waga + other.waga

    def __lt__(self, other):
        return self.waga < other.waga