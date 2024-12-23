f=open("s9.csv")
k=0
for i12 in range(12000):
    n=f.readline().split(";")
    n[-1]=n[-1][:-1]
    pov=[0]*7
    for i in range(7):
        pov[i]=n.count(n[i])
    chn=n
    for i in range(7):
        chn[i]=int(chn[i])
    if pov.count(2)==6 and pov.count(1)==1:
        nep=int(n[pov.index(1)])
        chn[pov.index(1)]=0
        if ((min(chn)+max(chn))/2) < nep:
            k+=1
print(k)
