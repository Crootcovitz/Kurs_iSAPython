def odwroc_string(zdanie):
    """
    Zwraca odwórcony string. Jeśli argument jest pustym stringiem lub None - zwraca None.
    :param zdanie: Zdanie do odwrócenia
    :return: Odwrócone zdanie lub None
    """
    if zdanie == '' or zdanie == None:
        return None
    else:
        return zdanie[::-1]

def main():
    imie = 'Ala'
    odwrocone_imie = odwroc_string(imie)
    spr_imie = imie[::-1]
    if odwrocone_imie == spr_imie:
        print(f'Imię {imie} zostało prawidłowe odwrócone na {odwrocone_imie}')
    else:
        print(f'Nieprawidłowo {spr_imie} != {odwrocone_imie}')

if __name__ =='__main__':
    main()
