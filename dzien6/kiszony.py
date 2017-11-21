import pickle

baza = [{"imie": 'Adam', 'nazwisko': 'Kowalski', 'wiek': 32},
{"imie": 'Anna', 'nazwisko': 'Nowak', 'wiek': 23},
{"imie": 'Jan', 'nazwisko': 'Nowacki', 'wiek': 34},
{"imie": 'Tomasz', 'nazwisko': 'Lato', 'wiek': 43}]

# zapisujemy

with open('baza.pckl', 'wb') as plik:
    pickle.dump(baza, plik)

# otwieramy

odczytana_baza = None

with open('baza.pckl', 'rb') as plik:
    odczytana_baza = pickle.load(plik, encoding='utf-8')
print(odczytana_baza)
