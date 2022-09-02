#C:\py3eg
Oddelovac = "=" 
film1 = {
'JMENO': 'Shawshank Redemption',
'HODNOCENI': 93,
'ROK': 1994,
'REZISER': 'Frank Darabont',
'HRAJI': ['Tim Robbins', 'Morgan Freeman'],
'STOPAZ': "144 min"
}

film2 = {
'JMENO': 'The Godfather',
'HODNOCENI': 92,
'ROK': 1972,
'REZISER': 'Francis Ford Coppola',
'HRAJI': ['Al Pacino', 'Marlon Brando'],
'STOPAZ': "175 min"
}

film3 = {
'JMENO': 'The Dark Knight',
'HODNOCENI': 90,
'ROK': 2008,
'REZISER': 'Christopher Nolan',
'HRAJI': ['Christian Bale', 'Heath Ledger'],
'STOPAZ': "152 min"
}
# I. KROK
# Vytvorim novy (prazdny) slovnik + oddelovac

film0 = {}

# II. KROK
# Vlozime klice (opet zatim prazdne)
film0["Jmeno"] = None
film0["Hodnoceni"] = None
film0["Rok"] = None
film0["Reziser"] = None

# III. KROK
# Doplnime hodnoty klicu
# Primo + update() metodou
# Kombinace s input()

film0["Jmeno"] = "Shawshank Redemption"
film0["Reziser"] = "Frank Darabont"
film0.update({"Hodnoceni": "93"})
film0.update({"Rok": "1994"})

# IV. KROK
# Vytvorime dalsi dva klice s hodnotami
# Klic *STOPAZ* odstranime pomoci metody *pop*
# Z klice *HRAJI* odstranime pomoci funkce *del*
film0["Hraji"] = ("Tim Robbins", "Morgan Freeman")
film0["Stopaz"] = "144 min"
film0.pop("Stopaz")
del film0["Hraji"]
# V. KROK
# Vytvorime novy slovnik *filmova_db*
filmova_db = dict()
# Nestujeme dva zbyvajici slovniky ze zadani
filmova_db[film1["JMENO"]] =  film1
filmova_db[film2["JMENO"]] =  film2

# VI. KROK
# Vytvorime pomyslneho interpreta nasi db
# Ten predstavi nase filmy
print(Oddelovac)
print("Vítejte")
print(Oddelovac)


# VII. KROK
# Vyzkousime metodu slovniku .get()
vyber = input("Vyberte film z nabídky: ")

print(filmova_db.get(vyber, "Vami zadany film neni v db"))

# VIII. KROK
# Vyzkousime metodu slovniku .setdefault()
import pprint

