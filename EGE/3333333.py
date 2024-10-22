def f(n):
    try:
        if n<2:
            return 1
        if n>=2 and n%3==0:
            return f(n/3)+1
        if n>=2 and n%3!=0:
            return f(n-2)+5
    except:
        pass
for n in range(10000):
    if f(n)!=None and f(n)==73:
        print(n)
        break
