from pprint import pprint

pracownicy = [
    {'imię': 'Waldermar', 'wiek': 30, 'pensja': 3300.00},
    {'imię': 'Marta', 'wiek': 23, 'pensja': 4200.00},
    {'imię': 'Zdzisław', 'wiek': 56, 'pensja': 5300.00}
]

# liczby = [34, 48, 51, 98, 45, 8 , 71, 56]
# print(sorted(liczby))
# liczby.sort()
# print(liczby)



prac_posortowani = sorted(pracownicy,
                          key=lambda element_listy: element_listy['pensja'],
                          reverse=True)

pprint(pracownicy)
print(25*'-')
pprint(prac_posortowani)
print(25*'-')
class Pracownik(object):
    def __init__(self, imie, wiek, pensja):
        self.imie =imie
        self.wiek = wiek
        self.pensja = pensja
    def __str__(self):
        return f'{self.imie} {self.wiek} {self.pensja}'
    def __repr__(self):
        return f'{self.imie} {self.wiek} {self.pensja}'
    def __lt__(self, other):
        return self.wiek < other.wiek

p1 = Pracownik('Waldemar', 30, 3300.0)
p2 = Pracownik('Marta', 23, 4200.0)
p3 = Pracownik('Zdzisław', 56, 5300.0)
# dzięki __str__
print(p1)
lista_p = [p1, p2, p3]
# dzięki __repr__
print(lista_p)
print(25*'-')
# dzięki __lt__
pprint(sorted(lista_p))
# dzięki lambda - nie trzeba zmieniać klasy przy zmianie klucza do sortowania
pprint(sorted(lista_p, key=lambda p: p.pensja))
