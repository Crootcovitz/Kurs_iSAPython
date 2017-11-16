# w docstringu argument w [], jeśli nie jest wymagany
def dodaj_imie(imie, baza=None):
    '''Dodaje imię do bazy; jeśli baza nie istnieje,
    tworzy nową
    (str, [list]) -> list'''
    if baza == None:
        baza = []
    imie = imie.upper()
    baza.append(imie)
    return baza


anglicy = dodaj_imie('john')
print(anglicy)
francuzi = dodaj_imie('antoin')
print(francuzi)
rosjanie = dodaj_imie('masza')
print(rosjanie)