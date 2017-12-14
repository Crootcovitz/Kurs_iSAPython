import dzien7.secrets
from tools.poczta import Poczta

nadawca = Poczta(dzien7.secrets.login, dzien7.secrets.haslo)
odbiorcy = ['crootcovitz@gmail.com', 'mateusz_dutkiewicz@poczta.fm']
temat = 'Drzewo'
tresc = 'Wiadomość testowa.'
fotki = ['../tools/drzewo.jpg']

nadawca.wyslij_wiadomosc(odbiorcy, temat, tresc, pliki=fotki)
