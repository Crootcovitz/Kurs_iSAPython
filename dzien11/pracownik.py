class Pracownik(object):

    ilosc_instancji = 0
    roczna_podwyzka = 5

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        Pracownik.ilosc_instancji += 1

    @classmethod
    def zmien_roczna_podwyzke(cls, nowa_wartosc):
        if type(nowa_wartosc) != type(int):
            return
        if nowa_wartosc > 18:
            cls.roczna_podwyzka = 18
        else:
            cls.roczna_podwyzka = nowa_wartosc

    @staticmethod
    def sprawdz_pesel(pesel):
        if len(pesel) != 11:
            print('pesel nieprawidłowy')
        else:
            print('pesel OK')

    def __str__(self):
        return f'Pracownik {self.nazwisko} ma {self.stawka} PLN.'

    def __del__(self):
        Pracownik.ilosc_instancji -= 1
        print(f'Pracownik {self.nazwisko} został zwolniony.')
