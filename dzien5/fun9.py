# wypisz spr czy liczby w zakresie
liczby = [2,4324,25,43,4,5765,756,7,3425,325,364]

# x - tak
# y - nie

def czy_w_zakresie(liczba, zakres=range(100)):
    '''
    Sprawdza, czy podana liczba jest w zakresie
    :param liczba: liczba do sprawdzenia
    :param zakres: range
    :return: None
    '''
    if liczba in zakres:
        print(f'{liczba} - Yes')
    else:
        print(f'{liczba} - No')

# pętla może się też znaleźć w funkcji
for x in liczby:
    czy_w_zakresie(x)