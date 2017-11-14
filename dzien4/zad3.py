#daj listę z unikalnymi wartościami
lista_a = [10, 20, 332, 23, 234, 10, 435, 35, 234, 20, 4938, 435]

lista_b = []

for i in lista_a:
    if i not in lista_b:
        lista_b.append(i)

#lista_b = sorted(lista_b)

posortowane = sorted(lista_b)
print(lista_b)
print(posortowane)
