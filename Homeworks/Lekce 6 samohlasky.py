sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'

souhlasky = "aeiouy"
pocet = {"samo": 0, "souh": 0}

for pismeno in sentence:
    if not pismeno.isalpha():
        continue
    if pismeno.lower() in souhlasky:
        pocet["souh"] += 1
    else:
        pocet["samo"] += 1

print('No. consonants: ' , str(pocet['souh']) , ' | No. vowels: ' , str(pocet['samo']))
