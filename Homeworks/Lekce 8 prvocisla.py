
# Definice fce list_primes
def list_primes(n):
    nums = list(range(2, n+1))
    vysledek = set()
    while nums:
        i= nums.pop(0)
        vysledek.add(i)
        for num in nums:
            if num % i ==0:
                nums.remove(num)
    return vysledek

# Definice fce is_prime
def is_prime(n):
    return n in list_primes(n)

# Volani fce is_prime
print(is_prime(23))