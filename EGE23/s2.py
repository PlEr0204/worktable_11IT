def f(st, x):
    if st>x:
        return 0
    if st==x:
        return 1
    if st<x:
        return f(st+1, x)+f(st+2, x)+f(st+4,x)
print(f(21,30))
