sciezka = 'tekst1.txt'

plik = open(sciezka, 'r')

tresc = plik.read()
print(tresc)

plik.close()