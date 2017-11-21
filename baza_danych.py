baza_danych = []


def dodanie_rekordu(tytul, rok, ocena):
    """
    Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param ocena: Ocena
    :return: None
    """
    w_bazie = False
    for wpis in baza_danych:
        if tytul in wpis and rok in wpis:
            w_bazie = True
    if w_bazie == False:
        baza_danych.append([tytul, rok, ocena])
        print(f'Pomyślnie dodano {tytul}({rok}) do bazy danych.')
    else:
        print(f'{tytul}({rok}) już istnieje w bazie danych.')


def usun_rekord(tytul, rok):
    """
    Usuwa rekord z bazy danych, lub informuje o jego braku.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :return: None
    """
    w_bazie = False
    for wpis in baza_danych:
        if tytul in wpis and rok in wpis:
            baza_danych.remove(wpis)
            w_bazie = True
    if w_bazie == False:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        print(f'Pomyślnie usunięto {tytul}({rok}) z bazy danych.')


def spr(tytul, rok):
    """
    Sprawdza, czy wpis znajduje się w bazie danych.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :return: None
    """
    w_bazie = False
    for wpis in baza_danych:
        if tytul in wpis and rok in wpis:
            w_bazie = True
    if w_bazie == False:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        print(f'{tytul}({rok}) istnieje w bazie danych.')


def zmiana_oceny(tytul, rok, ocena):
    """
     Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param ocena: Ocena
    :return: None
    """
    w_bazie = False
    for wpis in baza_danych:
        if tytul in wpis and rok in wpis:
            baza_danych[baza_danych.index(wpis)][2] = ocena
            w_bazie = True
    if w_bazie == False:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        print(f'Pomyślnie zmieniono ocenę dla {tytul}({rok}).')


def pokaz(tytul, rok):
    """
    Pokazuje pojednyczy wpis z bazy danych.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :return: None
    """
    w_bazie = False
    for wpis in baza_danych:
        if tytul in wpis and rok in wpis:
            pokaz_indeks = baza_danych.index(wpis)
            w_bazie = True
    if w_bazie == False:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        print(f'{"Tytuł":40}{"Rok":6}{"Ocena":4}\n'
              f'{baza_danych[pokaz_indeks][0]:40}{baza_danych[pokaz_indeks][1]:6}{baza_danych[pokaz_indeks][2]:4}')


warunek = True
while warunek:
    inp = input('Program służy do modyfikowania bazy danych ocen filmów. Wybierz opcję:\n'
                ':Jeśli chcesz dodać wpis do bazy danych, wpisz ADD\n'
                ':Jeśli chcesz usunąć wpis z bazy danych, wpisz DEL\n'
                ':Jeśli chcesz sprawdzić, czy wpis już istnieje w bazie danych, wpisz CHECK\n'
                ':Jeśli chcesz zmienić ocenę filmu, wpisz CHNG\n'
                ':Jeśli chcesz sprawdzić ilość rekordów w bazie danych, wpisz LEN\n'
                ':Jeśli chcesz wyświetlić całą bazę danych, wpisz SHOW\n'
                ':Jeśli chcesz wyświetlić jeden wpis z bazy danych, wpisz SHOW1\n'
                ':Jeśli chcesz zakończyć program, wpisz EXIT\n')
    if inp == 'ADD':
        tytul1 = input('Podaj tytuł filmu\n')
        rok1 = input('Podaj rok premiery filmu\n')
        ocena1 = input('Podaj ocenę w filmu w skali od 1 do 10\n')
        dodanie_rekordu(tytul1, rok1, ocena1)
    elif inp == 'DEL':
        tytul2 = input('Podaj tytuł filmu\n')
        rok2 = input('Podaj rok premiery filmu\n')
        usun_rekord(tytul2, rok2)
    elif inp == 'CHECK':
        tytul3 = input('Podaj tytuł filmu\n')
        rok3 = input('Podaj rok premiery filmu\n')
        spr(tytul3, rok3)
    elif inp == 'CHNG':
        tytul4 = input('Podaj tytuł filmu\n')
        rok4 = input('Podaj rok premiery filmu\n')
        ocena4 = input('Podaj nową ocenę w filmu w skali od 1 do 10\n')
        zmiana_oceny(tytul4, rok4, ocena4)
    elif inp == 'LEN':
        print(f'W bazie danych znajduje się {len(baza_danych)} ocenionych flimów.')
    elif inp == 'SHOW':
        print(f'{"Tytuł":40}{"Rok":6}{"Ocena":4}')
        for i in range(0, len(baza_danych)):
            print(f'{baza_danych[i][0]:40}{baza_danych[i][1]:6}{baza_danych[i][2]:4}')
    elif inp == 'SHOW1':
        tytul5 = input('Podaj tytuł filmu\n')
        rok5 = input('Podaj rok premiery filmu\n')
        pokaz(tytul5, rok5)
    elif inp == 'EXIT':
        warunek = False
        print('Kończenie pracy programu...')
    else:
        print('Nie zrozumiałem. Spróbuj ponownie.')
