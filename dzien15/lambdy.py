def kapitalizuj(zdanie: str) -> str:
    zdanie = zdanie.strip
    return zdanie.capitalize()

print(kapitalizuj)

kap = lambda wyraz: wyraz.capitalize()
print(kap)

w = kap('ala ma kota')
print(w)

