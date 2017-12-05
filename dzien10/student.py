from dzien10.czlowiek import Czlowiek

class Student(Czlowiek):
    def __init__(self, indeks):
        super().__init__('anonimowy', 19)

    def ruszaj_sie(self):
        print('Nie chce mi się, jestem po imprezie.')

    def powiedz(self):
        print('Poproszę o tróję!')

    def swietuj_egzaminy(self):
        print('Na zdrowie!')
