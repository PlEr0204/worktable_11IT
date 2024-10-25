def f(st, x):
    if st<x:
        return 0
    if st==x:
        return 1
    if st>x:
        return f(st-2, x)+f(st//2,x)
print(f(38,16)*f(16,2))
