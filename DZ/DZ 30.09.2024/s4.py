a=input()

ans={}
while a!="END!":
    m=a.split()
    for i in range(len(m)):
        if m[i] not in ans:
            ans[m[i]]=1
        else: 
            ans[m[i]]+=1
    a=input()
print(*ans, sep="\n")

