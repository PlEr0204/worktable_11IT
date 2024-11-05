f=open("9.csv")
k=0
for j in f:
    n1=f.readline()
    n=n1[:-1].split(",")
    for i in range(len(n)):
        n[i]=int(n[i])
    if len(set(n))==len(n):
        maxch=max(n)
        minch=min(n)
        for r in range(len(n)):
            if n[r]==maxch or n[r]==minch:
                n[r]=0
        if (maxch+minch)*2>=sum(n):
            k+=1
print(k)