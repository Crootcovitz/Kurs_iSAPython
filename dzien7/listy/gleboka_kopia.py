import copy

nabial = ['jajka', 'mleko', 'twaróg']
chemia = ['domestos', 'płyn do naczyń', 'proszek do prania']
zakupy_listopad = [nabial, chemia]

zakupy_grudzien = copy.deepcopy(zakupy_listopad)
zakupy_styczen = copy.deepcopy(zakupy_listopad)

zakupy_grudzien[0].append('mąka')

print(f'Zakupy listopad: {zakupy_listopad}.')
print(f'Zakupy grudzień: {zakupy_grudzien}.')
print(f'Zakupy styczeń:  {zakupy_styczen}.')