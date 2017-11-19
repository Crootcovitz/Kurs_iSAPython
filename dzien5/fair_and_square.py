def fair_and_square(od, do):
    """
    Sprawdza, ile liczb w podanym zakresie (włącznie z górną granicą) jest palindromami i kwadratami palindromów.
    :param od: dolna granica zakresu
    :param do: górna granica zakresu
    :return: ilość liczb spełniających warunek
    """
    licznik = 0
    for i in range(od, do+1):
        pierw = i**0.5
        if pierw.is_integer() == False:
            pass
        elif str(i) == str(i)[::-1] and str(int(pierw)) == str(int(pierw))[::-1]:
            licznik += 1
    return licznik


zakres1 = int(input('Podaj dolną granicę zakresu:\n'))
zakres2 = int(input('Podaj górną granicę zakresu:\n'))
odpowiedz = fair_and_square(zakres1, zakres2)
print(f'W zakresie od {zakres1} do {zakres2} jest {odpowiedz} liczb fair and square.')