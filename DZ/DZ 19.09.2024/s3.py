def prost(n):
    m=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            m.add(i)
            m.add(n//i)
    return sorted(m)
k=0
for i in range(1000000, 2000000000000000000):
    if k==5:
        break
    ans=prost(i)
    ans1=[]
    for j in range(len(ans)):
        if ans[j]%2==0:
            ans1.append(ans[j])
    if len(ans1)==5:
        print(i, sum(ans1))
        k+=1