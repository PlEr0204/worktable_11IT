ans=[]
for n in range(3,3000):
    s="3"+n*"5"
    while ("333" in s) or ("555" in s):
        if "555" in s:
            s=s.replace("555","3",1)
        else:
            s=s.replace("333","5",1)
    s=int(s)
    print(s)
    sum1=0
    while s!=0:
        sum1+=s%10
        s=s//10
    ans.append(sum1)
print(ans)
print(max(ans))