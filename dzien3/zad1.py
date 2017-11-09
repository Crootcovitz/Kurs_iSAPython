#oblicz, czy rok jest przestępny
#podzielny przez 4, ale nie przez 100, ale podzielny przez 400
rok=int(input('Podaj rok:\n'))

if rok%400==0:
    print(f'Rok {rok} jest przestępny.')
elif rok%4==0 and rok%100!=0:
    print(f'Rok {rok} jest przestępny.')
else:
    print(f'Rok {rok} nie jest przestępny.')
