seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]

res = {}

for i in seq:
    res[str(i)] = res.setdefault(str(i),0) + 1 

print(res) 