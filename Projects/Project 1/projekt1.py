'''
author = Ondřej Hrabina
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

oddelovac = "*" * 30
print(oddelovac)
print("Vítejte!")
jmeno = input("Zadejte uživatelské jméno: ",) 
heslo = input("Zadejte heslo: ")

uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = (jmeno, heslo)
hodnoty = uzivatele.items()

#test, zda je uživatel registrován
if user in hodnoty: 
    print("Jste přihlášeni")
else:
    print("Nejste registrováni")
print(oddelovac)
#vybereme text
print("Jsou k dispozici 3 testy k analýze.")
raw_text = TEXTS[int(input("Zvolte čílo v rozsahu 1 až 3: "))-1]
print(oddelovac)
#separujeme jednotlivá slova
raw_slova =raw_text.split()

#počet slov
title = []
for slovo in raw_slova:
    if slovo.istitle() and slovo.isalpha():
        title.append(slovo)
pocet = len(title)
print("V textu je ", pocet, "slov.")
#slova psaná velkými písmeny
upper = []
for slovo in raw_slova:
    if slovo.isupper():
        upper.append(slovo)
pocet_upper = len(upper)
print("V textu začíná", pocet_upper, "slov velkým písmenem.")
#slova psaná malými písmeny
lower = []
for slovo in raw_slova:
    if slovo.islower():
        lower.append(slovo)
pocet_lower = len(lower)
print("V textu je psáno", pocet_lower, "slov malým písmenem.")
#počet čísel
cisla = []
for slovo in raw_slova:
    if slovo.isdigit():
        cisla.append(slovo)

pocet_cisel = len(cisla)
print("V textu se vyskytuje", pocet_cisel, "čísel(a).")

#graf
seznam = []
for slovo in raw_slova:
    seznam.append(len(slovo))

s_seznam = sorted(seznam)

delky = {}

for i in s_seznam:
    delky[i] = delky.get(i, 1) + 1

for i in delky:
    print(i, "*" * delky[i], delky[i])


#součet čísel
soucet = 0
for i in cisla:
    soucet = soucet + int(i) 
print(oddelovac)
