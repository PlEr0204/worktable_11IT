from functools import lru_cache
@lru_cache(256)
def F(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return n*(n-1) + F(n-2)
print(F(2023)-F(2021)-2*F(2020)-F(2019))
