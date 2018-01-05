import openpyxl
from openpyxl.styles import PatternFill
import os
import re

def ekstrakcja(wyniki):
    with open(wyniki, 'r') as plik:
        dataline = re.compile('\w\s')
        plytka = []
        for linia in plik.readlines():
            if dataline.match(linia) is not None:
                plytka.append(linia.split())
    return plytka


def wypisz(plytki, ilosc, ws):
    for plytka, liczba in zip(plytki, range(ilosc)):
        for wiersz in range(0, 9):
            for kolumna in range(0,13):
                if wiersz == 0:
                    if kolumna == 0:
                        a1 = ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1)
                        a1.fill = PatternFill(start_color='FFFF0000',
                            end_color='FFFF0000',
                            fill_type='solid')
                    else:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1, value=kolumna)
                else:
                    if kolumna == 0:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1, value=plytka[wiersz - 1][kolumna])
                    else:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1, value=float(plytka[wiersz - 1][kolumna]))


cwd = os.getcwd()
wb = openpyxl.Workbook()
# ws = wb.active

arkusze = {}
ilosc_arkuszy = int(input('Ile antygenów?\n'))
for i in range(1, ilosc_arkuszy + 1):
    nazwa_arkusza = input(f'Podaj nazwę antygenu nr {i}:\n')
    arkusze[nazwa_arkusza] = wb.create_sheet(nazwa_arkusza)

liczba_plytek = int(input('Podaj liczbę płytek na antygen:\n'))
wyniki = {}
for key in arkusze.keys():
    wyniki[key] = []
    for plytka in range(1, liczba_plytek + 1):
        nazwa_pliku = input(f'Podaj nazwę pliku dla płyki nr {plytka} dla antygenu {key} (pamiętaj o rozszerzeniu .txt):\n')
        sciezka = os.path.join(cwd, nazwa_pliku)
        wyniki[key].append(ekstrakcja(sciezka))

for key in arkusze.keys():
    ws = wb[key]
    wypisz(wyniki[key], liczba_plytek, ws)
del wb['Sheet']
wb.save(r'C:\Users\Dudek\Desktop\test.xlsx')
# print(os.getcwd())
