from functools import lru_cache
@lru_cache(128)
def f(n):
    if n>=10000:
        return n
    if n<10000 and n%4==0:
        return n/4+f(n/4+2)
    if n<10000 and n%4!=0:
        return 1+f(n+2)
print(f(174)-f(3))