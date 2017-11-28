import os

file_path = 'dane.txt'

if os.path.exists(file_path):
    print('Ścieżka istnieje, otwieram plik.')
    with open(file_path, 'r') as file:
        print(file.read())
else:
    print('Ścieżka nie istnieje!')