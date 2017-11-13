temperatura = input('Podaj temperaturę (np. 35C lub 100F):\n')

wartosc = float(temperatura[:-1])
typ = temperatura[-1]

if typ == 'C':
    nowa_wartosc = wartosc * (9 / 5) + 32
    nowy_typ = 'F'
    print(f'Podana temperatura w {nowy_typ} to {nowa_wartosc} stopni.')
elif typ == 'F':
    nowa_wartosc = (wartosc - 32) * (5/9)
    nowy_typ = 'C'
    print(f'Podana temperatura w {nowy_typ} to {nowa_wartosc:.{4}} stopni.')
