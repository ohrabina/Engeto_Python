#C:\py3eg

# Vstupni hodnoty
jmeno = input("Zadejte své jméno:", )
vyska = int(input("Zadejte výšku:", ))
vaha = int(input("Zadejte váhu:", ))

# Vypocet
bmi = vaha/(vyska*vyska)


# Vytvor promennou kategorie a prirad ji pomoci podminek
kategorie = ''
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'


# Vytiskni odpoved s vysledkem

print(jmeno, "tvé BMI je", str(bmi) + ", což spadá do kategorie", kategorie + ".")