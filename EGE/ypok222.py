from functools import lru_cache
@lru_cache(128)
def f( n ):
    global m
    m.append(n+1)
    if n > 1:
        m.append(n+5)
        f(n-1)
        f(n-2)
m=[]
for i in range(1000000, 1500000):
    f(i)
    if sum(m)>1000000:
        print(i, sum(m))
        break
    else:
        m=[]