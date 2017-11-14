prawidlowe = False

while not prawidlowe:
    nazwisko = input('Podaj nazwisko drukowanymi literami lub Q aby zakończyć:\n')

    if nazwisko.upper() == 'Q':
        print('Do widzenia.')
        quit()
    elif nazwisko.isalpha():
        if nazwisko.isupper():
            prawidlowe = True

print('Gratulacje, jesteś zarejestrowany.')