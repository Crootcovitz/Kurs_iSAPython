sciezka = 'tekst1.txt'

tekst = """To jest mój tekst. To
jest kolejna linijka tekstu,
 a to kolejna"""

with open(sciezka, 'w', encoding='utf-8') as plik:
    print(plik.tell())
    plik.write(tekst)
    plik.seek(0)
    # plik.read()

