#C:/py3eg

print("Dobrý den, vepište čísla:")
cislo1 = int(input("Vepište první číslo: ", ))
cislo2 = int(input("Vepište první číslo: ", ))

power = True
while power == True: 

    operace = str(input('''

sčítání = sc
odečítání = od
dělení = de
násobení = na
ukončení = off
Vyberte operaci:
'''))

    if operace == 'sc':
        print(str(cislo1), '+', str(cislo2), '=', str(cislo1 + cislo2))

    elif operace == 'od':
        print(str(cislo1), '-', str(cislo2), '=', str(cislo1 - cislo2))

    elif operace == 'de':
        print(str(cislo1), '/', str(cislo2), '=', str(cislo1 / cislo2))

    elif operace == 'na':
        print(str(cislo1), '*', str(cislo2), '=', str(cislo1 * cislo2))

    elif operace == 'off':
       print('Kalkulačka byla vypnuta')
       power = False
        