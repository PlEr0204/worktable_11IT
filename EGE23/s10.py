def prost(n):
    m=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            m.add(i)
            m.add(n/i)
    return sum(m)
def f(st, x):
    if st>x:
        return 0
    if st==x:
        return 1
    if st<x:
        return f(st+1, x)+f(prost(st),x)
print(f(2,24))

