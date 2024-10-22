def f(n):
    try:
        if n<3:
            return n+1
        if n>=3 and n%2==0:
            return f(n-2)+n-2
        if n>=3 and n%2!=0:
            return f(n+2)+n+2
    except:
        pass
for i in range(10,100):
    print(f(i))