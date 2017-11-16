def dodaj_imie(imie, baza=[]):
    imie = imie.upper()
    baza.append(imie)
    return baza

# imiona = ['ANNA', 'DAMIAN']
#
# imiona = dodaj_imie('andrzej', imiona)
# imiona = dodaj_imie('marek', imiona)
# print(imiona)


anglicy = dodaj_imie('john')
print(anglicy)
francuzi = dodaj_imie('antoin')
print(francuzi)
rosjanie = dodaj_imie('masza')
print(rosjanie)

# Python tworzy nowy obiekt tylko przy pierwszym wywołaniu,
# potem używa tego, co stworzył przy wykorzystywaniu argumentu
# domyślnego