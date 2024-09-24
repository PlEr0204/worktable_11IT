f=open("17 (3).txt")
n=[int(x) for x in f.readlines()]
a=[]
for i in range(len(n)):
    if abs(n[i])%10==6:
        a.append(n[i])
k=0
ans=[]
for i in range(len(n)-1):
    if (abs(n[i])%10==6 and abs(n[i+1])%10!=6) or (abs(n[i])%10!=6 and abs(n[i+1])%10==6):
        if (n[i]**2+n[i+1]**2)<(min(a))**2:
            k+=1
            ans.append(n[i]**2+n[i+1]**2)
print(k, len(ans), max(ans))