from dzien9.samochod import Samochod
from dzien9.silnik import Silnik

silnik_v4 = Silnik(1998, 'benzyna')

beemka = Samochod('BMW', '3')

beemka.silnik = silnik_v4

print(beemka.silnik)

beemka.silnik.wlaczony = True