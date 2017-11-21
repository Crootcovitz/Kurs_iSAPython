osoby = {}

rekordy = [{"imie": 'Adam', 'nazwisko': 'Kowalski', 'wiek': 32},
{"imie": 'Anna', 'nazwisko': 'Nowak', 'wiek': 23},
{"imie": 'Jan', 'nazwisko': 'Nowacki', 'wiek': 34},
{"imie": 'Tomasz', 'nazwisko': 'Lato', 'wiek': 43}]

for indeks, rekord in enumerate(rekordy):
    osoby[indeks] = rekord

print(osoby)

najw_indeks = max(osoby.keys())
print(najw_indeks)

osoby[najw_indeks+1] = {"imie": 'Kamil', 'nazwisko': 'Kowal', 'wiek': 28}