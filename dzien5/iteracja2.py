rzeczy = ('pisak', 'długopis', 'szklanka', 'portfel', 'myszka')
kolory = ['czerwony', 'zielony', 'niebieski', 'fioletowy']

# x jest koloru: y

# while

indeks = 0
dlugosc = min(len(rzeczy), len(kolory))

while indeks < dlugosc:
    print(f'{rzeczy[indeks]} jest koloru: {kolory[indeks]}')
    indeks += 1

print(15*'-')
# for + zip

for rzecz1, kolor in zip(rzeczy, kolory):
    print(f'{rzecz1} jest koloru: {kolor}')
