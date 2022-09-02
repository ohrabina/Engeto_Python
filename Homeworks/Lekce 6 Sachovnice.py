size = 10
symbols = ["#", " "]

desk = []

for radek in range(size):
    line = []
    for cell in range(size):
        i = (radek + cell) % len(symbols)
        line.append(symbols[i])
    desk.append("".join(line))

print("\n".join(desk))