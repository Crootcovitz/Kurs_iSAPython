#po podaniu nazwy miesiąca podaj ilość dni w miesiącu
miesiac=input('Podaj nazwę miesiąca:\n')

if miesiac=='kwiecień' or\
miesiac=='czerwiec' or\
miesiac=='wrzesień' or\
miesiac=='listopad':
    print(f'Miesiąc {miesiac} ma 30 dni.')
elif miesiac=='luty':
    print(f'Miesiąc {miesiac} ma 28 lub 29 dni')
else:
    print(f'Miesiąc {miesiac} ma 31 dni.')