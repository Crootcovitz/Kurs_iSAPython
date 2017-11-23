import dzien7.podfolder.odwracacz

def czy_palindrom(wyraz):
    """Sprawdza, czy podany string jest palindromem.
    (str)->bool
    """
    wyraz = wyraz.upper()
    odwrocony = dzien7.podfolder.odwracacz.odwroc_string(wyraz)
    if wyraz == odwrocony:
        return True
    else:
        return False


print(czy_palindrom('kajak'))