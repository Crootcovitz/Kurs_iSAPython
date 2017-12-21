liczby = [1,2,3,4,5]

def kwadraty_lista(lista: list) -> list:
    temp = []
    for x in lista:
        temp.append(x**2)
    return temp

kw_lista = kwadraty_lista(liczby)

print(liczby)
print(kw_lista)

def kwadraty_generator(lista: list):
    for x in lista:
        yield x**2

kw_generator = kwadraty_generator(liczby)

print('-------------------------------')
print(liczby)
print(kw_generator)
# print(next(kw_generator))
# print(next(kw_generator))
# print(next(kw_generator))
# print(next(kw_generator))
# print(next(kw_generator))

for y in kw_generator:
    print(y)