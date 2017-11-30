def znajdz_wpis(tytul, rok, baza_danych):
    """
    Sprawdza, czy dany wpis znajduje się w bazie danych
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param baza_danych: Baza danych
    :return: Wpis lub None
    """
    for wpis in baza_danych:
        if tytul == wpis[0] and rok == wpis[1]:
            do_zwrotu = wpis
            break
        else:
            do_zwrotu = None
    return do_zwrotu

def dodanie_rekordu(tytul, rok, ocena, baza_danych):
    """
    Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param ocena: Ocena
    :param baza_danych: Baza danych
    :return: None
    """
    wpis = znajdz_wpis(tytul, rok, baza_danych)
    if wpis == None:
        baza_danych.append([tytul, rok, ocena])
        print(f'Pomyślnie dodano {tytul}({rok}) do bazy danych.')
    else:
        print(f'{tytul}({rok}) już istnieje w bazie danych.')


def usun_rekord(tytul, rok, baza_danych):
    """
    Usuwa rekord z bazy danych, lub informuje o jego braku.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param baza_danych: Baza danych
    :return: None
    """
    wpis = znajdz_wpis(tytul, rok, baza_danych)
    if wpis == None:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        baza_danych.remove(wpis)
        print(f'Pomyślnie usunięto {tytul}({rok}) z bazy danych.')


def spr(tytul, rok, baza_danych):
    """
    Sprawdza, czy wpis znajduje się w bazie danych.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param baza_danych: Baza danych
    :return: None
    """
    wpis = znajdz_wpis(tytul, rok, baza_danych)
    if wpis == None:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        print(f'{tytul}({rok}) istnieje w bazie danych.')


def zmiana_oceny(tytul, rok, ocena, baza_danych):
    """
     Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param ocena: Ocena
    :param baza_danych: Baza danych
    :return: None
    """
    wpis = znajdz_wpis(tytul, rok, baza_danych)
    if wpis == None:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        baza_danych[baza_danych.index(wpis)][2] = ocena
        print(f'Pomyślnie zmieniono ocenę dla {tytul}({rok}).')


def pokaz(tytul, rok, baza_danych):
    """
    Pokazuje pojednyczy wpis z bazy danych.
    :param tytul: Tytuł filmu
    :param rok: Rok premiery
    :param baza_danych: Baza danych
    :return: None
    """
    wpis = znajdz_wpis(tytul, rok, baza_danych)
    if wpis == None:
        print(f'Brak {tytul}({rok}) w bazie danych.')
    else:
        pokaz_indeks = baza_danych.index(wpis)
        print(f'{"Tytuł":40}{"Rok":6}{"Ocena":4}\n'
              f'{baza_danych[pokaz_indeks][0]:40}{baza_danych[pokaz_indeks][1]:6}{baza_danych[pokaz_indeks][2]:>5}')
