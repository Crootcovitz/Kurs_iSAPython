#fizz buzz

'''
for i in range(1, 101):
    # if i % 3 == 0 and i % 5 == 0:
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
k = 1
while k <= 100:
    if k % 3 == 0 and k % 5 == 0:
        print('FizzBuzz')
    elif k % 3 == 0:
        print('Fizz')
    elif k % 5 == 0:
        print('Buzz')
    else:
        print(k)
    k += 1
'''
for liczba in range(1, 101):
    if liczba % 3 == 0:
        print('Fizz', end='')
    if liczba % 5 == 0:
        print('Buzz', end='')
#da się jeszcze inaczej: jak?
    if liczba % 3 != 0 and liczba % 5 != 0:
        print(liczba, end='')
    print('\n', end='')



