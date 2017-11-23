for x in range(10):
    if x**2 > 100:
        print(f'Kwadrat {x} jest większy od 100.')
        break
else:
    print('Żaden kwadrat nie jest większy od 100.')

print('Koniec.')