import requests

def pobierz(link, sciezka):

    response = requests.get(link)

    if response.status_code == 200:

        bajty = 0

        try:
            with open(sciezka, 'wb') as plik:
                for part in response.iter_content(100000):
                    ilosc = plik.write(part)
                    bajty += ilosc
        except FileNotFoundError:
            bajty = 99999

    print(f'Zapisano {bajty} bajtów.')

def main():
    link = 'http://img.bazarek.pl/123802/10056/3482431/168820038350193e403b116.jpeg'
    pobierz(link, 'drzewo.jpg')

if __name__ == '__main__':
    main()