from dzien12.alternatywny_kons import Pracownik

prac1 = Pracownik('Adam', 'Kowalski', 13)

prac2 = Pracownik.Pracownik('Jan', 'Nowak')
print(prac2)

prac1.pesel = 46854455555
print(prac1.pesel)
print(Pracownik.__dict__)
print(prac1.__dict__)
print(prac2.__dict__)