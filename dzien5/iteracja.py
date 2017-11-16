rzeczy = ('pisak', 'długopis', 'szklanka', 'portfel', 'myszka')

# przedmiot: x ma indeks nr: y

# while
indeks = 0
# żeby funckja len() nie liczyła długości przy każdym przejściu pętli
dlugosc = len(rzeczy)
while indeks < dlugosc:
    print(f'Przedmiot: {rzeczy[indeks]} ma indeks nr: {indeks}')
    indeks += 1

print(15*'-')

# for

indeks2 = 0
for rzecz in rzeczy:
    print(f'Przemiot: {rzecz} ma indeks nr: {indeks2}')
    indeks2 += 1

print(15*'-')

# for + enumerate

for indeks3, przedmiot in enumerate(rzeczy):
    print(f'Przedmiot: {przedmiot} ma indeks nr: {indeks3}')