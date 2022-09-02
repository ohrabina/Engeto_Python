#C:\py3eg

# Zadany string
muj_string = 'Abc@abc.cz a Matous@1234.cz jsou naše emailové adresy'

# Rozdel string
rozdeleny_string = muj_string.split()

# Tisk promenne 'rozdeleny_string'
print(rozdeleny_string)

emaily = list()
emaily.append(rozdeleny_string[0])
emaily.append(rozdeleny_string[2])
# Tisk promenne 'emaily'
print(emaily)

# Ziskani domen
domena01 = emaily[0].split("@")[1]
domena02 = emaily[1].split("@")[1]

# Rozdel domeny podle znaku '.' a uloz je do stejne prommene
domena01 = domena01.split(".")[0]
domena02 =domena02.split(".")[0]

# Spoj promenne 'domena01' a 'domena02' s promennou 'bez_cisel'
bez_cisel = ''
# Dopln podminkovy vyraz pro 'domena01'
if domena01.isalpha():
    bez_cisel = bez_cisel.join(domena01)
    print("Domena byla přidána!")


else:
    print('Doména', domena01, 'nebyla přidána, protože obsahuje čísla!')

# Dopln podminkovy vyraz pro 'domena02'
if domena02.isalpha():
    bez_cisel = bez_cisel.join(domena02)
    print("Domena byla přidána!")

else:
    print('Doména', domena02, 'nebyla přidána, protože obsahuje čísla!')

# ZDE NIC NEDOPLNUJ, jde o nasi kontrolu :)
if (len(bez_cisel) + 1) % 4 == 0:
    print('Bezva, další zkouška úspěšně za tebou. Jen tak dál!')
else:
    print('Bohužel, někde máš chybku. Pokud si nevíš rady, mrkni se dolů na řešení.')