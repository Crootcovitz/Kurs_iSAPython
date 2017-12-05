from dzien10.zwierze import Zwierze

class Czlowiek(Zwierze):
    def __init__(self, nazwa, wiek):
        super().__init__(nazwa)
        self.wiek = wiek

    def ruszaj_sie(self):
        print(f'{self.nazwa.capitalize()} ruszył się.')

    def powiedz(self):
        print(f'Cześć, jestem {self.nazwa.capitalize()}.')
