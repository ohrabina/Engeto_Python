def my_gdc(a,b):
    while b >1:
        r = a % b
        if not r:
            break
        a,b = b, r
    return b

print(my_gdc(10,20))
