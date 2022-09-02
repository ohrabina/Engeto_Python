#C:\py3eg

# Nas slovnik
data = {
	'uzivatel1': 'heslo',
	'Marek': '1234',
	'Danko': 'qwert',
			}

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input("Zadejte jméno: ", )
heslo = input("Zadejte heslo: ", )


# Podminkovy vyraz
if  data.get(jmeno) != heslo:
	print("'Heslo, nebo uživatelské jméno je špatně!'")

elif  data.get(jmeno) == heslo:
	print("Povolení pokračovat!")