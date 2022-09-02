#C:\py3eg

# Prirazeni promennych
str1 = 'New York'
str2 = 'Yorkshire'

# Najde spolecne prvky

spolecne = set(str1) & set(str2) 

# Najde unikatni prvky

unikatni = set(str1) - set(str2)

# Najde nesdilene prvky

nesdilene = set(str1) ^ set(str2)

# Najde vsechny prvky

vsechny = set(str1) | set(str2)

# Vypis vsechno
print(spolecne)
print(unikatni)
print(nesdilene)
print(vsechny)