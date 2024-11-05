def f(st, x, k):
    if st>x:
        return 0
    if st==x and k==7:
        return 1
    if st==x and k!=7:
        return 0
    if st<x:
        return f(st+1, x, k+1)+f(st+2, x, k+1)+f(st+3, x, k+1)
z=f(3, 22, 0)        
print(z)