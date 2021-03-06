import pickle
from baza import Baza

baza_danych = Baza()


warunek = True
while warunek:
    inp = input('Program służy do modyfikowania bazy danych ocen filmów. Wybierz opcję:\n'
                ':Jeśli chcesz wczytać bazę danych z pliku, wpisz LOAD\n'
                ':Jeśli chcesz dodać wpis do bazy danych, wpisz ADD\n'
                ':Jeśli chcesz usunąć wpis z bazy danych, wpisz DEL\n'
                ':Jeśli chcesz sprawdzić, czy wpis już istnieje w bazie danych, wpisz CHECK\n'
                ':Jeśli chcesz zmienić ocenę filmu, wpisz CHNG\n'
                ':Jeśli chcesz sprawdzić ilość rekordów w bazie danych, wpisz LEN\n'
                ':Jeśli chcesz wyświetlić całą bazę danych, wpisz SHOW\n'
                ':Jeśli chcesz wyświetlić jeden wpis z bazy danych, wpisz SHOW1\n'
                ':Jeśli chcesz zapisać bazę danych do pliku, wpisz SAVE\n'
                ':Jeśli chcesz zakończyć program, wpisz EXIT\n')
    if inp == 'LOAD':
        plik_baza = input('Podaj ścieżkę do pliku:\n')
        try:
            with open(plik_baza, 'rb') as plik:
                baza_danych = pickle.load(plik)
            print('Pomyślnie wczytano bazę danych.')
        except FileNotFoundError:
            print('Taki plik nie istnieje.')
    elif inp == 'ADD':
        tytul1 = input('Podaj tytuł filmu\n')
        rok1 = input('Podaj rok premiery filmu\n')
        ocena1 = input('Podaj ocenę w filmu w skali od 1 do 10\n')
        baza_danych.dodanie_rekordu(tytul1, rok1, ocena1)
    elif inp == 'DEL':
        tytul2 = input('Podaj tytuł filmu\n')
        rok2 = input('Podaj rok premiery filmu\n')
        baza_danych.usun_rekord(tytul2, rok2)
    elif inp == 'CHECK':
        tytul3 = input('Podaj tytuł filmu\n')
        rok3 = input('Podaj rok premiery filmu\n')
        baza_danych.spr(tytul3, rok3)
    elif inp == 'CHNG':
        tytul4 = input('Podaj tytuł filmu\n')
        rok4 = input('Podaj rok premiery filmu\n')
        ocena4 = input('Podaj nową ocenę w filmu w skali od 1 do 10\n')
        baza_danych.zmiana_oceny(tytul4, rok4, ocena4)
    elif inp == 'LEN':
        print(f'W bazie danych znajduje się {len(baza_danych)} ocenionych flimów.')
    elif inp == 'SHOW':
        print(f'{"Tytuł":40}{"Rok":6}{"Ocena":4}')
        for i in range(0, len(baza_danych)):
            print(f'{baza_danych[i].tytul:40}{baza_danych[i].rok:6}{baza_danych[i].ocena:>5}')
    elif inp == 'SHOW1':
        tytul5 = input('Podaj tytuł filmu\n')
        rok5 = input('Podaj rok premiery filmu\n')
        baza_danych.pokaz(tytul5, rok5)
    elif inp == 'SAVE':
        plik_do_zapisu = input('Podaj ścieżkę do zapisania pliku:\n')
        try:
            with open(plik_do_zapisu, 'wb') as plik:
                pickle.dump(baza_danych, plik, -1)
            print('Pomyślnie zapisano bazę danych do pliku.')
        except FileNotFoundError:
            print('Podana ścieżka prowadzi do nieistniejącego folderu.')
    elif inp == 'EXIT':
        warunek = False
        print('Kończenie pracy programu...')
    else:
        print('Nie zrozumiałem. Spróbuj ponownie.')
