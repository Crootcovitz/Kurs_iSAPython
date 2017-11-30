class Samochod(object):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.jedzie = None
        self.silnik = None

    def ruszaj(self):
        self.jedzie = True
        print(f'{self.marka} ruszył.')


    def zatrzymaj(self):
        self.jedzie = False
        print(f'{self.marka} zatrzymał się.')