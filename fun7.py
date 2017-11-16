imie = 'Ola'

def wypisz_imie():
# global lepiej nie używać
    global imie
    duze_imie = imie.upper()
    return duze_imie


print(imie)
print(wypisz_imie())