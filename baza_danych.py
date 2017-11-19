baza_danych = []


def dodanie_rekordu(rekord1, rekord2, rekord3):
    """
    Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
    :param rekord1: Tytuł filmu
    :param rekord2: Rok premiery
    :param rekord3: Ocena
    :return: None
    """
    w_bazie1 = False
    for wpis1 in baza_danych:
        if rekord1 in wpis1 and rekord2 in wpis1:
            w_bazie1 = True
    if w_bazie1 == False:
        baza_danych.append([rekord1, rekord2, rekord3])
        print(f'Pomyślnie dodano {rekord1}({rekord2}) do bazy danych.')
    else:
        print(f'{rekord1}({rekord2}) już istnieje w bazie danych.')


def usun_rekord(rekord1, rekord2):
    """
    Usuwa rekord z bazy danych, lub informuje o jego braku.
    :param rekord1: Tytuł filmu
    :param rekord2: Rok premiery
    :return: None
    """
    w_bazie2 = False
    for wpis2 in baza_danych:
        if rekord1 in wpis2 and rekord2 in wpis2:
            baza_danych.remove(wpis2)
            w_bazie2 = True
    if w_bazie2 == False:
        print(f'Brak {rekord1}({rekord2}) w bazie danych.')
    else:
        print(f'Pomyślnie usunięto {rekord1}({rekord2}) z bazy danych.')


def spr(rekord1, rekord2):
    """
    Sprawdza, czy wpis znajduje się w bazie danych.
    :param rekord1: Tytuł filmu
    :param rekord2: Rok premiery
    :return: None
    """
    w_bazie3 = False
    for wpis3 in baza_danych:
        if rekord1 in wpis3 and rekord2 in wpis3:
            w_bazie3 = True
    if w_bazie3 == False:
        print(f'Brak {rekord1}({rekord2}) w bazie danych.')
    else:
        print(f'{rekord1}({rekord2}) istnieje w bazie danych.')


def zmiana_oceny(rekord1, rekord2, rekord3):
    """
     Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
    :param rekord1: Tytuł filmu
    :param rekord2: Rok premiery
    :param rekord3: Ocena
    :return: None
    """
    w_bazie4 = False
    for wpis4 in baza_danych:
        if rekord1 in wpis4 and rekord2 in wpis4:
            baza_danych[baza_danych.index(wpis4)][2] = rekord3
            w_bazie4 = True
    if w_bazie4 == False:
        print(f'Brak {rekord1}({rekord2}) w bazie danych.')
    else:
        print(f'Pomyślnie zmieniono ocenę dla {rekord1}({rekord2}).')


def pokaz(rekord1, rekord2):
    """
    Pokazuje pojednyczy wpis z bazy danych.
    :param rekord1: Tytuł filmu
    :param rekord2: Rok premiery
    :return: None
    """
    w_bazie5 = False
    for wpis5 in baza_danych:
        if rekord1 in wpis5 and rekord2 in wpis5:
            pokaz_indeks = baza_danych.index(wpis5)
            w_bazie5 = True
    if w_bazie5 == False:
        print(f'Brak {rekord1}({rekord2}) w bazie danych.')
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
