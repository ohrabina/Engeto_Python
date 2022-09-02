"""Lekce #8 - Uvod do programovani, obesenec"""
import random
# I. KROK
# Hlavni funkce + vymyslet postup
def hlavni():
    hrac = pridej_hrace()
    hadane_slovo = vyber_slovo()
    tajne_slovo, zbyvajici_tahy = schovej_slovo(hadane_slovo)
    while zbyvajici_tahy:
        zbyvajici_tahy = herni_kolo(
            hrac,
            tajne_slovo,
            zbyvajici_tahy,
            hadane_slovo
        )
        posouzeni_stavu_hry(tajne_slovo, hrac, zbyvajici_tahy)
# II. KROK
# Pridame hrace
def pridej_hrace():
    return input("ZADEJTE JMENO HRACE: ")
# III. KROK
# Zvolime slovo pro hadani + nacteme jej
def vyber_slovo():
    with open("slova.txt", "r") as txt:
        obsazena_slova = txt.read().split("\n")
        return random.choice(obsazena_slova)
# IV. KROK
# Schovame jej!
def schovej_slovo(slovo):
    return len(slovo) * ["_"], round(1.4 * len(slovo), 0)
# V. KROK
# Vypisujeme stav hry
def vypis_stav_hry(hr, post, tahy):
    zprava = f"HRAC: {hr}, STAV: {' '.join(post)} , ZBYVA: {tahy}"
    oddelovac = "-" * len(zprava)
    print(oddelovac, zprava, oddelovac, sep="\n")
# VI. KROK
# Hrac hada pismeno
def hadane_pismeno():
    return input("HADEJ PISMENO: ")
# VII. KROK
# Posouzeni hadaneho pismena
def posouzeni_hadani(pismeno, slovo, tajne_slovo):
    for index, pism in enumerate(slovo):
        if pism in pismeno:
            tajne_slovo[index] = pism
# VIII. KROK
# Prubeh kazdeho kola
def herni_kolo(hrac, tajne_slovo, zbyvajici_tahy, hadane_slovo):
    vypis_stav_hry(hrac, tajne_slovo, zbyvajici_tahy)
    hracuv_odhad = hadane_pismeno()
    posouzeni_hadani(hracuv_odhad, hadane_slovo, tajne_slovo)
    zbyvajici_tahy -= 1
    return zbyvajici_tahy
# IX. KROK
# Zaverecny vystup
def posouzeni_stavu_hry(tajne_slovo, hrac, zbyvajici_tahy):
    if "_" not in tajne_slovo:
        vypis_stav_hry(hrac, tajne_slovo, zbyvajici_tahy)
        print(f"VYBORNE! {hrac}, UHODL JSI!")
        exit()
    elif "_" in tajne_slovo and zbyvajici_tahy == 0:
        print(f"PROHRAL JSI! {hrac}, SNAD PRISTE!")
        exit()
hlavni()