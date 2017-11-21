sciezka = 'tekst1.txt'

tekst = 'Dopisana linijka tekstu.'

with open(sciezka, 'r+') as plik:
    plik.read()
    # print(plik.tell())
    pozycja = plik.tell()
    plik.seek(pozycja - 1)
    ostatni_znak = plik.read()
    print(ostatni_znak)

    if ostatni_znak != '\n':
        plik.write('\n' + tekst + '\n')
    else:
        plik.write(tekst + '\n')