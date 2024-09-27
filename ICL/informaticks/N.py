n=list(input().split())
sl={}
for x in n:
    if x in sl:
        sl[x]+=1
    else:
        sl[x]=1
for x1 in sl:
    if x1>maxch:
        