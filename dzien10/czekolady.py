from dzien10.czekolada import Czekolada
from dzien10.producent import Producent

prod1 = Producent('Milka', 'Zurich')

czeko1 = Czekolada('z orzechami', prod1, 400)
czeko2 = Czekolada('z rodzynkami', prod1, 600)

print(czeko1)
print(czeko2)

print(czeko1 + czeko2)
print(czeko1 > czeko2)