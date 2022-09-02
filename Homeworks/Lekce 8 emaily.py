my_str='''Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Mauris vulputate lacus id eros consequat tempus.
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id
        tiger123@email.cz auctor massa molestie at. Nunc tristique
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas
        massa purus, ultricies a dictum ut, dapibus vitae massa.
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor
        nec molestie quis, auctor a quam. Quisque b2b@money.fr
        pretium dolor et tempor feugiat. Morbi libero lectus,
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est.
        Maecenas gravida turpis nec ultrices aliquet.'''
# Funkce pro posbirani emailu ze stringu

def vytazeni(vstup):
    words = vstup.split()
    emails = []
    for word in words:
        if '@' in word:
            emails.append(word)
    return emails
# Funkce pro extrahovani emailu obsahujici cisla
def cisla(emails):
    num_mails = []
    for email in emails:
        if obsahuje_cislo(email):
            num_mails.append(email)
    return num_mails
def obsahuje_cislo(_string):
    for num in range(10):
        if str(num) in _string:
            return True
    return False
    # Funkce pro extrahovani domen vsech emailu
def domena(emails):
    domeny = []
    for email in emails:
        domeny.append(email.split('@')[-1])
    return domeny

def main():
    vysledek = {"emails with nums": None, "domains": None}
    emails = vytazeni(my_str)
    vysledek["emails with nums"] = cisla(emails)
    vysledek["domains"] = domena(emails)
    print(vysledek)
    return vysledek

main()