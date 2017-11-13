data = input('Podaj datę (dd.mm):\n')

dzien = int(data[:2])
miesiac = int(data[3:5])

if (dzien >= 21 and miesiac == 3) or (miesiac > 3 and miesiac < 6) or (dzien < 22 and miesiac == 6):
    print('Jest wiosna.')
elif (dzien >= 22 and miesiac == 6) or (miesiac > 6 and miesiac < 9) or (dzien < 23 and miesiac == 9):
    print('Jest lato.')
elif (dzien >= 23 and miesiac == 9) or (miesiac > 9 and miesiac < 12) or (dzien < 22 and miesiac == 12):
    print('Jest jesień.')
elif (dzien >= 22 and miesiac == 12) or miesiac < 3 or (dzien < 21 and miesiac == 3):
    print('Jest zima.')
