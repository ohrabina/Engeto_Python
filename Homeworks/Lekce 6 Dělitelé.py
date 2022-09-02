start=int(input("Start: "))
stop= int(input("Stop: "))
devisor=int(input("Devisor: "))

if devisor == 0:
    print("Nelze dělit nulou!")

print("Čísla v rozmezí (",start,",", stop, ")", "dělitelná", devisor)

vysledek = []

rozmezi = list(range(start, stop+1))

for cislo in rozmezi:
    if cislo % devisor == 0:
        vysledek.append(cislo)

print(vysledek)