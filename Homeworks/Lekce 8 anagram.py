def all_anagrams(words):
    if words:
        result = True
        seq = sorted(words.pop())
        for word in words:
            if sorted(word) != seq:
                result = False
            else:
                result = True
    else:
        result = False                           
    return result
# Slova
words = ['ship','hips','name']
# Volani fce
print( all_anagrams(words) )