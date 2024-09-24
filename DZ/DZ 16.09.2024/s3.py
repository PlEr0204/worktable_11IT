f=open("17 (2).txt")
n=[int(x) for x in f.readlines()]
a=[]
for i in range(len(n)):
    if n[i]%2!=0:
        a.append(n[i])
k=0
ans=[]
for i in range(len(n)-1):
    if (n[i]%5==0 and n[i+1]<(sum(a)/len(a))) or (n[i+1]%5==0 and n[i]<(sum(a)/len(a))):
        k+=1
        ans.append(n[i]+n[i+1])
print(k, len(ans), max(ans))