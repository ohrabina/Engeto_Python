time = str(input("Vložte čas: ", ))

hours = time.split(":")[0]
mins = time.split(":")[1]

adjusted_time = hours if int(hours)==12 else str(int(hours)%12)

cas = ["AM", "PM"][int(hours)>=12]

print("Převedený čas: ", adjusted_time, mins, cas, ".")