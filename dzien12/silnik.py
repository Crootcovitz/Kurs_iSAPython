class Silnik(object):
    """
    Silnik
    """

    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.__spalanie = None
        self.__co2 = 0.8

    def podaj_emisje(self, wartosc):
        if self.__co2 <1:
            self.__co2 *= wartosc
        else:
            self.__co2 = wartosc*0.8

    def emisja(self):
        if self.__co2 > 20:
            return 20
        else:
            return self.__co2

    @property
    def spalanie(self):
        print('Jestem w property.')
        if self.__spalanie != None:
            return self.__spalanie*0.9
        else:
            return 0

    @property
    def co2(self):
        return self.__co2

    @spalanie.setter
    def spalanie(self, value):
        print('Ustawiam wartość w setterze.')
        if value > 8:
            self.__spalanie = 7.8
        else:
            self.__spalanie = 0.9 * value

    @co2.setter
    def co2(self, value):
        self.__co2 = value