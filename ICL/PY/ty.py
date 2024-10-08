from itertools import *
sogl="БРХТК"
k=0
def prov1(n):
    for i in range(7):
        if n[i]=="А" and n[i+1]=="А":
            return False
    return True
def prov(n):
    for i in range(7):
        if n[i] in sogl and n[i+1] in sogl:
            return False
    return True
for x in permutations("БАРХАТКА", r=8):
    if prov(x) and prov1(x):
        k+=1
print(k)
