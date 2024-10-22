def f(n):
    try:
        if n<2:
            return 1
        if n>=2 and n%3==0:
            return f(n/3)-1
        if n>=2 and n%3!=0:
            return f(n-1)+7
    except:
        pass
for n in range(100000):
    if f(n)!=None and f(n)==111:
        print(n)
        break
