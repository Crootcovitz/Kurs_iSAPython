def pole_kwadratu(bok):
    pole = bok*bok
    return pole


powierzchnia = pole_kwadratu(234)
print(f'Powierzchnia wynosi {powierzchnia}')
print(pole_kwadratu(2387))
# wywoływanie bez nawiasów zwraca adres w pamięci
print(pole_kwadratu)

x = pole_kwadratu
print(x(2))
