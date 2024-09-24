def prost(n):
    m=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            m.add(i)
            m.add(n//i)
    return sorted(m)
n=int(input())
for i in range(n):
    ch=int(input())
    maxdel=-1
    for j in range(ch):
        ans1=prost(j)
        if len(ans1)>maxdel:
            maxdel=len(ans1)
    for j1 in range(ch):
        if len(prost(j1))==maxdel:
            print(j1)
            break
    
            