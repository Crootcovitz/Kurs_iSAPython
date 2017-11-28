file_path = 'dane.txt'

try:
    with open(file_path, 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print('Podany plik nie istnieje!, e')
except Exception as e:
    print('Uuups, nastąpił jakiś błąd.', e)
finally:
    print('Tan funkcja zawsze się wykona.')

try:
    print('To jest blok try.')
    raise ValueError('Sam tworzę wyjątek! typ ValueError')
except ValueError as e:
    print('Złapałem wyjątek.', e)
finally:
    print('Zawsze się wykonam.')