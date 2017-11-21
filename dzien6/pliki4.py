sciezka = 'tekst1.txt'

with open(sciezka, 'a') as plik:
    print(plik.tell())
    plik.write('Moja kolejna linijka.\n')