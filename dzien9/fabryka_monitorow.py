from dzien9.monitor import Monitor

monitor1 = Monitor('AOK', 19)
print(f'Monitor {monitor1.producent} ma przekątną {monitor1.przekatna} cali.')
monitor1.kolor = 'czerwony'
print(monitor1.kolor)

monitor2 = Monitor('Asus', 24)
print(f'Monitor {monitor2.producent} ma przekątną {monitor2.przekatna} cali.')
