#C:\py3eg

 # Pozdrav klienta
print('=' * 80)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print('=' * 80)

# Nabídni mu destinaci
print('We can offer you the following destinations:')
print('-' * 80)
print('''
1 - Prague | 1000
2 - Wien | 1100
3 - Brno | 2000
4 - Svitavy | 1500
5 - Zlin | 2300
6 - Ostrava | 3400
''')
print('-' * 80)

# Získej vstup uživatele o destinaci
selection = int(input('Please enter the destination number to select: '))

# Přiřaď proměnným příslušná data
DESTINATIONS = ['Prague', 'Wien','Brno','Svitavy','Zlin','Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Zkontroluj, zde byl vložen vhodný vstup
if not 0 < selection <= len(DESTINATIONS):
    print('Omlouváme se, ale poskytujeme cesty pouze do ' + (len(DESTINATIONS)) + ' destinations')
else:

# Získej data z proměnných podle vstupu uživatele
destination = DESTINATIONS[selection-1]
price = PRICES[selection-1]

# Spočítej cenu a zkontroluj, zda je vhodný aplikovat slevu pro zvolenou destinaci
if destination in DISCOUNT_25:
        print('Gratulujeme k 25% slevě do destinace ' + destination)
        input('Pro pokračování stiskněte ENTER')
        price =  price * 0.75
    print('=' * 80)
# Začni registraci

# Získej vstup uživatele o jeho osobních datech
name = input('NAME: ')
print('=' * 40)
surname = input('SURNAME: ')
print('=' * 40)
birth_year = input('YEAR of BIRTH: ')
print('=' * 40)
email = input('EMAIL: ')
print('=' * 40)
password = input('PASSWORD: ')
print('=' * 80)

if 2020 - int(birth_year) < 15:
    print('Omlouváme se, ale naše služby poskytujeme pouze plnoletým.')
# Zkontroluj, jestli email obsahuje zavináč - @
elif '@' not in email:
    print('Zadal jste neplatný formát emailu.')
# Zkontroluj, jestli heslo
# - má aspoň 8 znaků
# - nezačíná ani nekončí číslem
# - a obsahuje písmena i čísla
elif (password.isnumeric() or password.isalpha()
      or password[0].isnumeric() or password[-1].isnumeric()
      or len(password) < 8):
    print('''
    Heslo musí obsahovat:
    - písmena i čísla
    - minimálně 8 znaků
    - nemůže začínat a končit číslem
    Zadejte platné heslo
    ''')
else:
# Poděkuj uživateli použitím jeho jména a informuj jej/jí o provedení rezervace
    print('Děkujeme ' + name)
    print('Zpracovali jsme Vaši rezervaci do ' + destination)
    print('Celková cena je: ' + str(price))