
def my_min(cisla):
    minimal = cisla[0]
    for num in cisla[1:]:
        if num <= minimal:
            num = minimal
    return(minimal)

def my_max(cisla):
    maximal = cisla[0]
    for num in cisla[1:]:
        if num >= maximal:
            num = maximal
    return(maximal)

