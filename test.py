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


def wypisz(plytki, ilosc, ws, pliki):
    for plytka, liczba in zip(plytki, range(ilosc)):
        for wiersz in range(0, 9):
            for kolumna in range(0, 13):
                if wiersz == 0:
                    if kolumna == 0:
                        a1 = ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1, value=pliki[liczba])
                        a1.fill = PatternFill(start_color='FFFF0000',
                                              end_color='FFFF0000',
                                              fill_type='solid')
                    else:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1, value=kolumna)
                else:
                    if kolumna == 0:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1, value=plytka[wiersz - 1][kolumna])
                    else:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 1,
                                value=float(plytka[wiersz - 1][kolumna]))


def srednie(plytki, studzienki, powtorzenia, ws, opcja):
    for liczba in plytki:
        for wiersz in range(0, 9):
            for kolumna in range(0, int(int(studzienki[liczba][1]) / (8 * powtorzenia)) + 1):
                if wiersz == 0:
                    if kolumna == 0:
                        if opcja == '+':
                            a1 = ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 14 + int(studzienki[liczba][0]),
                                     value='średnia(+)')
                        elif opcja == '-':
                            a1 = ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 14 + int(studzienki[liczba][0]),
                                     value='średnia(-)')
                        elif opcja == 'co':
                            a1 = ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 14 + int(studzienki[liczba][0]),
                                     value='średnia(co)')
                        a1.fill = PatternFill(start_color='FFFF0000',
                                              end_color='FFFF0000',
                                              fill_type='solid')
                else:
                    if kolumna == 0:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 14 + int(studzienki[liczba][0]),
                                value=f'{ws.cell(row=wiersz +1, column = 1).value}')
                    else:
                        ws.cell(row=wiersz + 1 + 10 * liczba, column=kolumna + 14 + int(studzienki[liczba][0]),
                                value=f'=AVERAGE('
                                      f'{ws.cell(row=wiersz + 1 + 10 * liczba, column=(kolumna - 1) * powtorzenia + int(studzienki[liczba][0]) + 1).coordinate}:'
                                      f'{ws.cell(row=wiersz + 1 + 10 * liczba, column=(kolumna - 1) * powtorzenia + int(studzienki[liczba][0]) + 1 + powtorzenia - 1).coordinate})')
        zakres = f'{ws.cell(row=2 + 10 * liczba, column=14 + int(studzienki[liczba][0]) + 1).coordinate}:' \
                 f'{ws.cell(row=9 + 10 * liczba, column=int(studzienki[liczba][1])/(8 * powtorzenia) + 14 + int(studzienki[liczba][0])).coordinate}'
        return zakres


# def cutoff()
        # if opcja == 'co':
        #     a1 = ws.cell(row=1 + 10 * liczba,
        #                  column=int(studzienki[liczba][1]) / (8 * powtorzenia) + 1 + 14 + int(studzienki[liczba][0]),
        #                  value='cutoff')
        #     a1.fill = PatternFill(start_color='FFFF0000',
        #                           end_color='FFFF0000',
        #                           fill_type='solid')
        #     ws.cell(row=2 + 10 * liczba,
        #             column=int(studzienki[liczba][1]) / (8 * powtorzenia) + 1 + 14 + int(studzienki[liczba][0]),
        #             value=f'=AVERAGE('
        #                   f'{ws.cell(row=2 + 10 * liczba, column=14 + int(studzienki[liczba][0])).coordinate}:'
        #                   f'{ws.cell(row=9 + 10 * liczba, column=int(studzienki[liczba][1])/(8 * powtorzenia) + 14 + int(studzienki[liczba][0])).coordinate})'
        #                   f'+ 2 * (_xlfn.STDEVA('
        #                   f'{ws.cell(row=2 + 10 * liczba, column=14 + int(studzienki[liczba][0])).coordinate}:'
        #                   f'{ws.cell(row=9 + 10 * liczba, column=int(studzienki[liczba][1])/(8 * powtorzenia) + 14 + int(studzienki[liczba][0])).coordinate}))'
        #             )


cwd = os.getcwd()
wb = openpyxl.Workbook()

arkusze = {}
ilosc_arkuszy = int(input('Podaj liczbę antygenów:\n'))
for i in range(1, ilosc_arkuszy + 1):
    nazwa_arkusza = input(f'Podaj nazwę antygenu nr {i}:\n')
    arkusze[nazwa_arkusza] = wb.create_sheet(nazwa_arkusza)
del wb['Sheet']

liczba_plytek = int(input('Podaj liczbę płytek na antygen:\n'))
pliki = {}
wyniki = {}
for key in arkusze.keys():
    pliki[key] = []
    wyniki[key] = []
    for plytka in range(1, liczba_plytek + 1):
        nazwa_pliku = input(
            f'Podaj nazwę pliku dla płyki nr {plytka} dla antygenu {key} (pamiętaj o rozszerzeniu .txt):\n')
        sciezka = os.path.join(cwd, nazwa_pliku)
        pliki[key].append(nazwa_pliku)
        wyniki[key].append(ekstrakcja(sciezka))

for key in arkusze.keys():
    ws = wb[key]
    wypisz(wyniki[key], liczba_plytek, ws, pliki[key])

powtorzenia = int(input('Podaj liczbę powtórzeń dla jednej surowicy:\n'))
studzienki_pozytywne = {}
studzienki_negatywne = {}
studzienki_cutoff = {}

for key in arkusze.keys():
    plytki_pozytywne = input(f'Podaj numery płytek z antygenem {key}, w których znajdują się surowice pozytywne (oddielone spacją):\n')
    plytki_pozytywne = plytki_pozytywne.split()
    for i in range(len(plytki_pozytywne)):
        plytki_pozytywne[i] = int(plytki_pozytywne[i]) - 1
    plytki_negatywne = input(f'Podaj numery płytek z antygenem {key}, w których znajdują się surowice negatywne (oddzielone spacją):\n')
    plytki_negatywne = plytki_negatywne.split()
    for i in range(len(plytki_negatywne)):
        plytki_negatywne[i] = int(plytki_negatywne[i]) - 1
    plytki_cutoff = input(f'Podaj numery płytek z antygenem {key}, w których znajdują się surowice do obliczenia cutoff (oddzielone spacją):\n')
    plytki_cutoff = plytki_cutoff.split()
    for i in range(len(plytki_cutoff)):
        plytki_cutoff[i] = int(plytki_cutoff[i]) - 1

for key in arkusze.keys():
    studzienki_pozytywne[key] = []
    studzienki_negatywne[key] = []
    studzienki_cutoff[key] = []
    for plytka in range(plytki_pozytywne[-1] + 1):
        if plytka in plytki_pozytywne:
            plus = input(f'Podaj początkową kolumnę i liczbę studzienek, w których znajdują się surowice pozytywne'
                         f' na płytce nr {plytka + 1} dla antygenu {key} (oddzielone spacją):\n')
            studzienki_pozytywne[key].append(plus.split())
        else:
            studzienki_pozytywne[key].append('k')
    for plytka in range(plytki_negatywne[-1] + 1):
        if plytka in plytki_negatywne:
            minus = input(f'Podaj początkową kolumnę i liczbę studzienek, w których znajdują się surowice negatywne'
                          f' na płytce nr {plytka + 1} dla antygenu {key} (oddzielone spacją):\n')
            studzienki_negatywne[key].append(minus.split())
        else:
            studzienki_negatywne[key].append('k')
    for plytka in range(plytki_cutoff[-1] + 1):
        if plytka in plytki_cutoff:
            studzienki = input(
                f'Podaj początkową kolumnę i liczbę studzienek, w których znajdują się surowice do obliczenia cutoff'
                f' na płytce nr {plytka + 1} dla antygenu {key} (oddzielone spacją):\n')
            studzienki_cutoff[key].append(studzienki.split())
        else:
            studzienki_cutoff[key].append('k')

for key in arkusze.keys():
    ws = wb[key]
    zakres_plus = srednie(plytki_pozytywne, studzienki_pozytywne[key], powtorzenia, ws, '+')
    zakres_minus = srednie(plytki_negatywne, studzienki_negatywne[key], powtorzenia, ws, '-')
    zakres_co = srednie(plytki_cutoff, studzienki_cutoff[key], powtorzenia, ws, 'co')


# print(zakres_plus, zakres_minus, zakres_co)
wb.save(r'C:\Users\Dudek\Desktop\test.xlsx')
wb.close()
