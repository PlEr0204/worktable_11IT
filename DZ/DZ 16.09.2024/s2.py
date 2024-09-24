f=open("17 (1).txt")
n=[int(x) for x in f.readlines()]
k=0
ans=[]
for i in range(len(n)-1):
    if (n[i]-n[i+1])%60==0:
        k+=1
        ans.append(n[i]-n[i+1])
print(k, max(ans))