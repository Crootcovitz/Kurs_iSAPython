import binascii

with open('C:\\Users\\Dudek\\Desktop\\Kurs_Python\\iSAPython4\\dzien7\\treasure_inside', 'rb') as plik:
    plik_hex = binascii.hexlify(plik.read())
    znak1 = b'49454e44'
    znak2 = b'ffd8ff'
    znak3 = b'ffd9ffd8ff'
    koniec_png = 0
    poczatek_jpg1 = 0
    poczatki_reszty_jpg = []
    koniec_ostatniego_jpg = len(plik_hex)
    for i in range(0, len(plik_hex) - len(znak1)):
        if plik_hex[i:i + len(znak1)] == znak1:
            koniec_png = i + len(znak1)
            break
    for j in range(koniec_png, len(plik_hex) - len(znak2)):
        if plik_hex[j:j + len(znak2)] == znak2:
            poczatek_jpg1 = j
            break
    for k in range(poczatek_jpg1, len(plik_hex) - len(znak3)):
        if plik_hex[k:k + len(znak3)] == znak3:
            poczatki_reszty_jpg.append(k+4)

# print(koniec_png)
# print(poczatek_jpg1)
# print(poczatki_reszty_jpg)

plik_png = binascii.unhexlify(plik_hex[0:koniec_png])
plik_jpg1 = binascii.unhexlify(plik_hex[poczatek_jpg1:poczatki_reszty_jpg[0]])
plik_jpg2 = binascii.unhexlify(plik_hex[poczatki_reszty_jpg[0]:poczatki_reszty_jpg[1]])
plik_jpg3 = binascii.unhexlify(plik_hex[poczatki_reszty_jpg[1]:poczatki_reszty_jpg[2]])
plik_jpg4 = binascii.unhexlify(plik_hex[poczatki_reszty_jpg[2]:koniec_ostatniego_jpg])

with open('C:\\Users\\Dudek\\Desktop\\Kurs_Python\\iSAPython4\\dzien7\\plik_png.png', 'wb') as plik:
    plik.write(plik_png)
with open('C:\\Users\\Dudek\\Desktop\\Kurs_Python\\iSAPython4\\dzien7\\plik_jpg1.jpg', 'wb') as plik:
    plik.write(plik_jpg1)
with open('C:\\Users\\Dudek\\Desktop\\Kurs_Python\\iSAPython4\\dzien7\\plik_jpg2.jpg', 'wb') as plik:
    plik.write(plik_jpg2)
with open('C:\\Users\\Dudek\\Desktop\\Kurs_Python\\iSAPython4\\dzien7\\plik_jpg3.jpg', 'wb') as plik:
    plik.write(plik_jpg3)
with open('C:\\Users\\Dudek\\Desktop\\Kurs_Python\\iSAPython4\\dzien7\\plik_jpg4.jpg', 'wb') as plik:
    plik.write(plik_jpg4)
