#mamy podane 3 boki trójkąta. czy da się narysować trójkąt?
a=float(input('Podaj długość boku a:\n'))
b=float(input('Podaj długość boku b:\n'))
c=float(input('Podaj długość boku c:\n'))

if a+b>c and a+c>b and b+c>a:
    if a==b and a==c:
        print(f'Da się narysować trójkąt o bokach {a}, {b}, {c}. Jest to trójkąt równoramienny.')
    elif a==b or a==c or b==c:
        print(f'Da się narysować trójkąt o bokach {a}, {b}, {c}. Jest to trójkąt równoboczny.')
    else:
        print(f'Da się narysować trójkąt o bokach {a}, {b}, {c}. Jest to trójkąt różnoboczny.')
else:
    print(f'Nie da się narysować trójkątu o bokach {a}, {b}, {c}.')
