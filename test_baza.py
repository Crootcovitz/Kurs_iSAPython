from baza import Baza

baza = Baza()
baza[2] = baza.Wpis('a', 'b', 'c')
for i in baza.values():
    print(i.tytul)
cos = baza.znajdz_wpis('a', 'b')
print(cos.tytul)
baza.dodanie_rekordu('a', 'b', 'c')
baza.pokaz('a', 'b')

