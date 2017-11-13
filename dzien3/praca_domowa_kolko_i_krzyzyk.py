stan_gry = input('Podaj stan gry: x (krzyżyk), o (kółko) lub n (puste pole) ciągiem wierszami od góry.\n')

pole_1 = stan_gry[0]
pole_2 = stan_gry[1]
pole_3 = stan_gry[2]
pole_4 = stan_gry[3]
pole_5 = stan_gry[4]
pole_6 = stan_gry[5]
pole_7 = stan_gry[6]
pole_8 = stan_gry[7]
pole_9 = stan_gry[8]
nazwa_pola = None

if pole_1 == pole_2 and pole_1 == pole_3 and pole_1 != 'n':
    if pole_1 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_1}).')
elif pole_4 == pole_5 and pole_4 == pole_6 and pole_4 != 'n':
    if pole_4 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_4}).')
elif pole_7 == pole_8 and pole_7 == pole_9 and pole_7 != 'n':
    if pole_7 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_7}).')
elif pole_1 == pole_4 and pole_1 == pole_7 and pole_1 != 'n':
    if pole_1 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_1}).')
elif pole_2 == pole_5 and pole_2 == pole_8 and pole_2 != 'n':
    if pole_2 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_2}).')
elif pole_3 == pole_6 and pole_3 == pole_9 and pole_3 != 'n':
    if pole_3 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_3}).')
elif pole_1 == pole_5 and pole_1 == pole_9 and pole_1 != 'n':
    if pole_1 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_1}).')
elif pole_3 == pole_5 and pole_3 == pole_7 and pole_3 != 'n':
    if pole_3 == 'x':
        nazwa_pola = 'krzyżyk'
    else:
        nazwa_pola = 'kółko'
    print(f'Grę wygrywa {nazwa_pola} ({pole_3}).')
else:
    print('Brak zwycięzcy.')
