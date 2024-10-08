from itertools import product
p=[]
for x in product("01234567", repeat=3):
    if x[0]not in '035':
        p.append(x)
        print(x)
#print(p)