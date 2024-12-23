f=open("17.txt")
m=[int(x) for x in f.readlines()]
a=[]
ans=[]
for i in range(len(m)):
    if abs(m[i])%10==3 and len(str(m[i]))==5:
        a.append(m[i])
for i in range(len(m)-2):
    if abs(m[i])%10==3 or abs(m[i+1])%10==3 or abs(m[i+2])%10==3:
        if m[i]+m[i+1]+m[i+2]<=max(a):
            ans.append(m[i]+m[i+1]+m[i+2])
print(len(ans),max(ans))
