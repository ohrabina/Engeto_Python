#C:\py3eg

oddelovac = "=" * 60
oddelovac2 = "-" * 60
# Pozdrav klienta
print(oddelovac)
print("Welcome to the DESTINATIO, place where people plan their trips")
print(oddelovac)
# Nabídni mu destinace
print("We can offer you the following destinations:")
print(oddelovac2)

print('''
1 - Prague  | 1000
2 - Wien    | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
''')
print(oddelovac2)
# Získej vstup uživatele o destinaci
cislo = int(input("Please enter the destination number to select:", ))
# Přiřaď proměnným příslušná data
destinace = ["Prague", "Wien", "Brno", "Svitavy", "Zlín", "Ostrava"]
ceny = ["1000", "1100", "2000", "1500", "2300", "3400"]
# Získej data z proměnných podle vstupu uživatele
cil = destinace[cislo - 1]
cena = ceny [cislo - 1]
# Začni registraci
print(oddelovac)
print("Registration:")
print(oddelovac2)
print("In order to complete your reservations, please share few details about yourself with us.")
print(oddelovac2)
# Získej vstup uživatele o jeho osobních datech
jmeno = input("Zadejte jméno: ", )
prijmeni = input("Zadejte prijmeni: ", )
narozeni = input("Zadejte rok narozeni: ", )
email = input("Zadejte email: ", )
heslo = input("Zadejte heslo:", )

print("Jméno: ", jmeno)
print("Přijmení: ", prijmeni)
print("Rok narození: ", narozeni)
print("Emailová adresa: ", email)
print("Heslo: ", heslo)

print(oddelovac)

# Poděkuj uživateli použitím jeho jména a informuuj jej/jí o provedení rezervace
print("Děkujeme za rezervaci", jmeno)
print("Cena Vaší rezervace je ", cena, "Kč.")