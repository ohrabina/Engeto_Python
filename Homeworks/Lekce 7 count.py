# Definice funkce count

def count(cil, values):
    vysledek = 0

    for value in values:
        if value == cil:
            vysledek += 1
    return vysledek

# Nase data
names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark', 'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim',
'Mark', 'Mark', 'Bob', 'Mark']

# Pouziti funkce count a tisk vysledku

print(count('Bob', names))