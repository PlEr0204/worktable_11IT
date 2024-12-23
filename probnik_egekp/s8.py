from itertools import *
ans=0
for n in product("012345678",repeat=5):
    k=0
    for i in range(5):
        if n[i]=="5":
            k+=1
    if k==1:
        f=True
        for i in range(4):
            if n[i]==n[i+1]:
                f=False
        if f:
            ans+=1
            print(n)
print(ans)
