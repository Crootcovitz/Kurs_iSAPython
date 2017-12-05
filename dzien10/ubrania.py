class Ubranie(object):
    def __init__(self, nazwa, material, rozmiar):
        self.nazwa = nazwa
        self.material = material
        self.rozmiar = rozmiar
    def zaloz(self):
        print(f'{self.nazwa} założono.')

class But(Ubranie):
    def __init__(self, nazwa, material, rozmiar, wysokosc):
        super().__init__(nazwa, material, rozmiar)
        self.wysokosc = wysokosc

    def zaimpregnuj(self):
        print('Zaimpregnowano.')

class Szpilka(But):
    def __init__(self, nazwa, material, rozmiar, wysokosc):
        super().__init__(nazwa, material, rozmiar, wysokosc)

    def wywroc_sie(self):
        print('Aaa!')

class Pantofel(But):
    def __init__(self, nazwa, material, rozmiar, wysokosc):
        super().__init__(nazwa, material, rozmiar, wysokosc)

    def wygodnie(self):
        print('Tak, wygodnie.')

class OdziezWierzchnia(Ubranie):
    def __init__(self, nazwa, material, rozmiar, chlonnosc):
        super().__init__(nazwa, material, rozmiar)
        self.chlonnosc = chlonnosc

    def wypierz(self):
        print('Wyprano.')

class Plaszcz(OdziezWierzchnia):
    def __init__(self, nazwa, material, rozmiar, chlonnosc):
        super().__init__(nazwa, material, rozmiar, chlonnosc)

    def wygladaj_wspaniale(self):
        print('Wow!')



