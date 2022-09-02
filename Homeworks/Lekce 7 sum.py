# Definice funkce sum
def my_sum(hodnoty):
    vysledek = 0
    for hodnota in hodnoty:
        vysledek += hodnota
    return vysledek
# Data k secteni
data = [32,43,54,54,76,21,62,83,52,58]

# Pouziti a funkce sum na data a tisk vysledku

print(my_sum(data))