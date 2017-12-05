class Producent(object):
    def __init__(self, nazwa, miejscowosc):
        self.nazwa = nazwa
        self.miejscowosc = miejscowosc

    def __str__(self):
        return f'{self.nazwa} z {self.miejscowosc}.'