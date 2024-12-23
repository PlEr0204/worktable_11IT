def f(st,x):
    if st>x:
        return 0
    if st==16:
        return 0
    if st==x:
        return 1
    if st<x:
        return f(st+1,x)+f(st+3,x)+f(st**2,x)
print(f(3,20)*f(20,26))