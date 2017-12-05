from dzien10.zwierze import Zwierze

class Kot(Zwierze):
    def __init__(self, nazwa, kolor):
        super().__init__(nazwa)
        self.kolor = kolor

    def ruszaj_sie(self):
        print(f'Kotek {self.nazwa} ruszył się.')