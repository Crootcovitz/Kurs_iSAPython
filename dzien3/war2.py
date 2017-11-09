nazwisko=input('Podaj nazwisko:\n')
# print(type(nazwisko))
#jeśli w stringu są cyfry, napisać komunikat i przerwać proogram
if not nazwisko.isalpha():
    print('Muszą być tylko litery.')
    exit(99)

#usunąć whitespace'y z początku i końca
#naz_czyste=nazwisko.strip()
# nazwisko=nazwisko.strip()
#zamienić wszystkie litery na duże
naz_czyste=nazwisko.upper()
if naz_czyste[-1] == 'A':
    print('Chyba jesteś kobietą.')
elif naz_czyste.endswith('SKI'):
    print('Najprawdopodobniej jesteś mężczyzną.')
# elif nazwisko.isupper():
#     print('Chyba jesteś złośliwa :/')

print('Koniec programu')
