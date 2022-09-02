#C:\py3eg

muj_slovnik = dict()
novy_slovnik = dict()

# vloz klice 'jméno', 'přijmení' do 'muj_slovnik' a přidej libovolne hodnoty
muj_slovnik['jméno'] 	= 'Ondra'
muj_slovnik['přijmení'] 	= 'Hrabina'

# vytvor z tuple 'muj_tuple' slovnik do slovniku 'novy_slovnik'
muj_tuple = 'věk', 'email'

novy_slovnik = novy_slovnik.fromkeys(muj_tuple)

# dopln muj_slovnik o novy_slovnik

muj_slovnik.update(novy_slovnik)


# vypln klice 'věk' a 'mail'
muj_slovnik['věk'] = 29
muj_slovnik['email'] = 'a@b.com'

# TADY NIC NEPIŠ!! Slouží pro kontrolu :)
if (len(muj_slovnik) + 1) % 5 == 0 and '@' in muj_slovnik['email']:
	print('Paráda, metody slovníků ovládáš na jedničku, blahopřejeme!')
else:
	print('Bohužel jsi někde udělal chybku :(\nPodívej se ještě jednou na tabulku s metodami.\n\npozn. Obsahuje tvůj email "@"?')