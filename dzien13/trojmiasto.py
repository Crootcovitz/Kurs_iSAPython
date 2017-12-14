import requests
from bs4 import BeautifulSoup

adres = 'http://trojmiasto.pl'

response = requests.get(adres)

print(response.status_code)
# wyrzuci wyjątek, jeśli status nie jest równy 200
response.raise_for_status()

trojmiasto_zupa = BeautifulSoup(response.text, 'html.parser')

linki = trojmiasto_zupa.select('.news-list a')

# print(linki)

for link in linki:
    # print(link.getText())

    print(f"Wiadomość: {link.get('title')}")
    print(link.get('href'))
    print(20*'-'+'\n')