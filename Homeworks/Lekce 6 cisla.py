
inpt = input("Zadejte čílsla: ")

nums = inpt.split(",")
result = []

for cislo in nums:
    cislo = int(cislo.strip())
    result.append(cislo)

print("List: ", result)