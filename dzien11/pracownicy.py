from dzien11.pracownik import Pracownik

prac1 = Pracownik('John', 'Travolta', 50000)
print(prac1)

prac2 = Pracownik('John', 'Turturo', 30000)
print(prac2)

prac3 = Pracownik('John', 'Rambo', 90000)
print(prac3)

# print(prac1.roczna_podwyzka)
# print(prac2.roczna_podwyzka)
# print(prac3.roczna_podwyzka)
#
# prac1.roczna_podwyzka = 15
#
# print(prac1.roczna_podwyzka)
# print(prac2.roczna_podwyzka)
# print(prac3.roczna_podwyzka)
#
# Pracownik.roczna_podwyzka = 10
#
# print(prac1.roczna_podwyzka)
# print(prac2.roczna_podwyzka)
# print(prac3.roczna_podwyzka)
#
# del prac1.roczna_podwyzka
#
# print(prac1.roczna_podwyzka)
# print(prac2.roczna_podwyzka)
# print(prac3.roczna_podwyzka)
print(prac1.ilosc_instancji)
print(prac2.ilosc_instancji)
print(prac3.ilosc_instancji)

# del prac2

print(Pracownik.ilosc_instancji)
# usunięcie pozostałych pracowników następuje przy czyszczeniu pamięci po zakończeniu programu

print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

prac1.zmien_roczna_podwyzke(18)
# przyjęło się, że robi się to przez klasę
Pracownik.zmien_roczna_podwyzke(22)

print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

