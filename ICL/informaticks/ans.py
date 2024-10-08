from itertools import *
k1=0
for x in product("АБРТЫ", repeat=5):
    k1+=1
    k=0
    for j in range(5):
        if x[j]!="Ы":
            k+=1
    if k==5:
        print(k1, x)
