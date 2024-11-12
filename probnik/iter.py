from itertools import *
kans=0
for i in product("0123456789ABCDEF", repeat=8):
    k=0
    for j in range(8):
        if i[j]=="0":
            k+=1
    if k==2:
        k1=0
        for j1 in range(8):
            if i[j1] in "0123456789":
                k1+=1
        if k1<=4:
            kans+=1
print(kans)
