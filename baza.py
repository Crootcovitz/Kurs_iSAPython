class Baza(list):
    """
    Baza danych filmów.
    """
    def __init__(self):
        super().__init__()

    class Wpis(object):
        """
        Wpis w bazie danych filmów.
        """
        def __init__(self, tytul, rok, ocena):
            self.tytul = tytul
            self.rok = rok
            self.ocena = ocena

    def znajdz_wpis(self, tytul, rok):
        """
        Sprawdza, czy dany wpis znajduje się w bazie danych
        :param tytul: Tytuł filmu
        :param rok: Rok premiery
        :return: Wpis lub None
        """
        for wpis in self:
            if  tytul == wpis.tytul and rok == wpis.rok:
                do_zwrotu = wpis
                break
        else:
            do_zwrotu = None
        return do_zwrotu

    def dodanie_rekordu(self, tytul, rok, ocena):
        """
        Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
        :param tytul: Tytuł filmu
        :param rok: Rok premiery
        :param ocena: Ocena
        :return: None
        """
        wpis = self.znajdz_wpis(tytul, rok)
        if wpis == None:
            self.append(self.Wpis(tytul, rok, ocena))
            print(f'Pomyślnie dodano {tytul}({rok}) do bazy danych.')
        else:
            print(f'{tytul}({rok}) już istnieje w bazie danych.')

    def usun_rekord(self, tytul, rok):
        """
        Usuwa rekord z bazy danych, lub informuje o jego braku.
        :param tytul: Tytuł filmu
        :param rok: Rok premiery
        :return: None
        """
        wpis = self.znajdz_wpis(tytul, rok)
        if wpis == None:
            print(f'Brak {tytul}({rok}) w bazie danych.')
        else:
            self.remove(wpis)
            print(f'Pomyślnie usunięto {tytul}({rok}) z bazy danych.')

    def spr(self, tytul, rok):
        """
        Sprawdza, czy wpis znajduje się w bazie danych.
        :param tytul: Tytuł filmu
        :param rok: Rok premiery
        :return: None
        """
        wpis = self.znajdz_wpis(tytul, rok)
        if wpis == None:
            print(f'Brak {tytul}({rok}) w bazie danych.')
        else:
            print(f'{tytul}({rok}) istnieje w bazie danych.')

    def zmiana_oceny(self, tytul, rok, ocena):
        """
         Dodaje rekord do bazy danych, jeśli jeszcze go tam nie ma.
        :param tytul: Tytuł filmu
        :param rok: Rok premiery
        :param ocena: Ocena
        :return: None
        """
        wpis = self.znajdz_wpis(tytul, rok)
        if wpis == None:
            print(f'Brak {tytul}({rok}) w bazie danych.')
        else:
            wpis.ocena = ocena
            print(f'Pomyślnie zmieniono ocenę dla {tytul}({rok}).')

    def pokaz(self, tytul, rok):
        """
        Pokazuje pojednyczy wpis z bazy danych.
        :param tytul: Tytuł filmu
        :param rok: Rok premiery
        :return: None
        """
        wpis = self.znajdz_wpis(tytul, rok)
        if wpis == None:
            print(f'Brak {tytul}({rok}) w bazie danych.')
        else:
            print(f'{"Tytuł":40}{"Rok":6}{"Ocena":4}\n'
                  f'{wpis.tytul:40}{wpis.rok:6}{wpis.ocena:>5}')
