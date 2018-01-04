import openpyxl
from openpyxl.styles import PatternFill
import os
import re

cwd = os.getcwd()
wb = openpyxl.Workbook()
ws = wb.active
with open('EXP0035.txt', 'r') as plik:
    dataline = re.compile('\w\s')
    plytka = []
    for linia in plik.readlines():
        if dataline.match(linia) is not None:
            plytka.append(linia.split())
for wiersz in range(0, 9):
    for kolumna in range(0,13):
        if wiersz == 0:
            if kolumna == 0:
                a1 = ws.cell(row = wiersz + 1, column = kolumna + 1)
                a1.fill = PatternFill(start_color='FFFF0000',
                   end_color='FFFF0000',
                   fill_type='solid')
            else:
                a1 = ws.cell(row = wiersz + 1, column = kolumna + 1, value = kolumna)
        else:
            if kolumna ==0:
                ws.cell(row = wiersz + 1, column = kolumna + 1, value = plytka[wiersz - 1][kolumna])
            else:
                ws.cell(row = wiersz + 1, column = kolumna + 1, value = float(plytka[wiersz - 1][kolumna]))



wb.save(r'C:\Users\Dudek\Desktop\test.xlsx')
# print(os.getcwd())
