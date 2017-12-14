import os, shutil, send2trash

# print(shutil.disk_usage('C:\\'))

# pliki = os.listdir('..\\')

# for plik in pliki:
#     print(plik)

#usuwa plik
# os.unlink('..\\import pickle')

# send2trash.send2trash(ścieżka)

# os.walk()
ilosc = 0
for biezacy_folder, podfoldery, pliki in os.walk('..\\'):
    # print('Obecny katalog:', biezacy_folder)
    #
    # for podfolder in podfoldery:
    #     print(f'podfolder {podfolder} w katalogu {biezacy_folder}')

    for plik in pliki:
        # print(f'plik {plik} w folderze {biezacy_folder}')
        ilosc += 1

print(f'Jest {ilosc} plików.')