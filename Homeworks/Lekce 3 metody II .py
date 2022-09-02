#C:\py3eg

# slovniky
slovnik01 = {'jmeno': 'David', 'prijmeni': 'Novak', 'vek': 33}
slovnik02 = {'pismena': ['a', 'b', 'c', 'd'], 'cisla': [1,2,3,4,5]}
slovnik03 = {'zamestnanci': {'id01': 'Marek', 'id02': 'Matous', 'id03': 'Anna'}, 'adresy': {'id01': 'Brno', 'id02': 'Praha', 'id03': 'Praha'}}

# ziskej klice i hodnoty
klice_hodnoty = slovnik01.items()

# ziskej klice
klice = slovnik02.keys()

# ziskej hodnoty
hodnoty = slovnik03.values()

# VYZVA
# ziskej hodnoty z vnitrniho slovniku
vyzva = slovnik03['zamestnanci'].values()
print(vyzva)


# ZDE NIC NEPIŠ. Slouží pouze pro kontrolu :)
if len(klice_hodnoty) == 3 and len(klice) == len(hodnoty) and (int(len(vyzva)))%3 == 0:
	print('Skvělá práce! Zvládl jsi jak naši Challenge, tak procvičení celkově!')
elif len(klice_hodnoty) == 3 and len(klice) == len(hodnoty) or (int(len(vyzva)))%3 == 0:
	print('Dobrá práce! Ještě v tom jsou chybky, ale je s čím pracovat!')
else:
	print('Bohužel :(\nMrkni se na metody ještě jednou a pak zkus úlohu znovu.')