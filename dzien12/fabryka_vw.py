from dzien12.silnik import Silnik

silnik1 = Silnik(1600)
silnik1.podaj_emisje(23)

# nie ma dostępu do pseudoprywatnego pola
# silnik1.__co2

# name mangling
print(silnik1._Silnik__co2)

print(silnik1.spalanie)

silnik1.spalanie = 12
print(silnik1.spalanie)

