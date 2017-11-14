zdanie = input('Podaj jakieś zdanie: \n')

samogloski = 0
spolgloski = 0

for i in zdanie:
    if i.isalpha():
        if i in 'aeiouyąęóAEIOUYĄĘÓ':
            samogloski += 1
        else:
            spolgloski += 1

print(f'Samogłosek {samogloski}, spółgłosek: {spolgloski}')
