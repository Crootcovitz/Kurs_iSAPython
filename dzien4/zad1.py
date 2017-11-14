#obliczyć ilość l. parzystych i nieparzystych w zakresie

zakres = range(23746)

parzyste = 0
nieparzyste = 0

for i in zakres:
    if i % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f"Liczb parzystych: {parzyste}, liczb nieparzystych: {nieparzyste}.")