liczby = [1, 2, 3, 4, 5]

# list comprehension
liczby_kw = [x**2 for x in liczby]

print(liczby)
print(liczby_kw)

#list comprehension z warunkiem
kw_dla_parzystych = [x**2 for x in liczby if x % 2 == 0]
print(kw_dla_parzystych)

# tworzenie generatora
kwadraty = (x**2 for x in liczby)
print(kwadraty)

for i in kwadraty:
    print(i)
