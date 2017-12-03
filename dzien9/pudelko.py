class Pudelko(object):
    """
    Pudełko zapałek.
    """
    def __init__(self):
        self.material = 'karton'
        self.otwarte = False
        self.zapalka = self.Zapalka()

    def __str__(self):
        return 'Zwykłe pudełko zapałek.'

    def otworz(self):
        if not self.otwarte:
            self.otwarte = True
            print('Pudełko zapałek zostało otwarte.')
        else:
            print('Pudełko zapałek jest już otwarte.')

    def zamknij(self):
        if self.otwarte:
            self.otwarte = False
            print('Pudełko zapałek zostało zamknięte.')
        else:
            print('Pudełko zapałek jest już zamknięte.')

    def wyciagnij_zapalke(self, liczba=1):
        if self. otwarte and self.zapalka.w_pudelku > 0:
            self.zapalka.w_pudelku -= liczba
            self.zapalka.wolne += liczba
        elif self.zapalka.w_pudelku == 0:
            print('Pudełko jest już puste.')
        else:
            print('Najpierw otwórz pudełko.')

    class Zapalka(object):
        """
        Zapałka.
        """
        def __init__(self):
            self.material = 'drewno'
            self.zapalona = False
            self.w_pudelku = 100
            self.wolne = 0
            self.spalone = 0

        def __str__(self):
            return 'Drewniana zapałka.'

        def zapal(self):
            if not self.zapalona and self.wolne > 0:
                self.zapalona = True
                self.wolne -= 1
                print('Zapalono zapałkę.')
            elif self.wolne == 0:
                print('Najpierw wyciągnij zapałkę z pudełka.')
            else:
                print('Lepiej nie zapalać drugiej zapałki, kiedy pierwsza jeszcze płonie.')

        def zgas(self):
            if self.zapalona:
                self.zapalona = False
                self.spalone += 1
                print('Zgaszono zapałkę.')
            else:
                print('Żadna zapałka aktualnie nie płonie.')
