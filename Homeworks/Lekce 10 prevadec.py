def to_arab(roman):
    #zadefinuju jednotlivé čísla
    slozena = {'IV' :4, 'IX' :9, 'XL' :40, 'XC' :90, 'CD' :400, 'CM' :900}
    jednoducha = {'I' :1, 'V' :5, 'X' :10, 'L' :50, 'C' :100, 'D' :500, 'M' : 1000}
    vysledek = 0
    while roman:
        if roman[:2] in slozena:
            num = roman[:2]
            roman = roman[2:]
            cislo = slozena

        else:
            num = roman[:1]
            roman = roman[1:]
            cislo = jednoducha

        vysledek += cislo[num]

    return vysledek

def to_roman(num):
    cislo = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL', 50:'L',90:'XC',100:'C',400:'CD', 500:'D',900:'CM',1000:'M'}
    vysledek = ''

    for arab in sorted(cislo, reverse=True):
        roman = cislo[arab]
        vysledek += num // arab * roman
        num %= arab

    return vysledek

print(to_roman(55))

