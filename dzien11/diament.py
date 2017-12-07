class Zwierz(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def mow(self):
        print(f'Zwierzę {self.nazwa} nie mówi.')

    def ruszaj(self):
        print(f'Zwierzę {self.nazwa} rusza się.')

class Kon(Zwierz):
    def __init__(self, nazwa, umaszczenie):
        Zwierz.__init__(self, nazwa)
        self.umaszczenie = umaszczenie

    def mow(self):
        print(f'Koń {self.nazwa} mówi "iiiiiiihhhhhhhhaaaaaaaa!"')

    def ruszaj(self):
        print(f'Koń {self.nazwa} hasa po łące.')

class Osiol(Zwierz):
    def __init__(self, nazwa, st_upartosci):
        Zwierz.__init__(self, nazwa)
        self.st_upartosci = st_upartosci

    def ruszaj(self):
        print(f'Osioł {self.nazwa} nie chce się ruszyć przez najbliższe {self.st_upartosci} minuty.')

    def wypisz_upartosc(self):
        print(f'Upartość: {self.st_upartosci} minuty.')

class Mul(Kon, Osiol):
    def __init__(self, nazwa, umaszczenie):
        Kon.__init__(self, nazwa, umaszczenie)

