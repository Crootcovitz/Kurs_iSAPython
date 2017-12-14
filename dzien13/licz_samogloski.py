import sys
# Poda ścieżkę i listę argumentów.
# print(sys.argv)

if len(sys.argv) != 3:
    print('Błędna liczba argumentów.')
    exit()

zdanie = sys.argv[1]
litera = sys.argv[2]

# Sprawdza, czy zdanie jest stringiem - zwraca True lub wyjątek
assert isinstance(zdanie, str)
# Teraz PyCharm będzie podpowiadał metody dla zdania, bo wie, że to string
print(zdanie.count(litera))
