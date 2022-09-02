
def caesar(message, offset):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    encrypted=[]

    for char in message:

        if char.lower() not in alphabet:
            encrypted.append(char)
            continue

        position = alphabet.index(char.lower())

        index = (position+offset) % len(alphabet)

        if char.isupper():
            new_char = alphabet[index].upper()
        else:
            new_char = alphabet[index]

        encrypted.append(new_char)

    return ''.join(encrypted)

message = 'abc def ghi jkl mno pqr stu vwx Yz'

print(caesar(message,-2))

