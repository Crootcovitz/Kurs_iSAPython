from dzien11.pracownik import Pracownik

prac1 = Pracownik('John', 'Travolta', 50000)
print(prac1)

prac2 = Pracownik('John', 'Torturo', 30000)
print(prac2)

print('Dict prac1:')
print(prac1.__dict__)
print('\nDict prac2:')
print(prac1.__dict__)
print('\nDict klasa:')
print(Pracownik.__dict__)

prac1.roczna_podwyzka = 15

print('Dict prac1:')
print(prac1.__dict__)
print('\nDict prac2:')
print(prac1.__dict__)
print('\nDict klasa:')
print(Pracownik.__dict__)

