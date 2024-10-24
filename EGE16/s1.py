def f(n):
    if n>18:
        return n
    else:
        return 3*f(n+1)+n+8
print(f(9))