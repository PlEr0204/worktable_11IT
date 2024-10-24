def f(n):
    try:
        if n<=1:
            return n
        if n>1 and n%3==0:
            return n+f(n/3-1)
        if n>1 and n%3!=0:
            return n+f(n+3)
    except:
        pass
for n in range(10000):
    st=f(n)
    if st!=None and st>1000:
        print(n)
        break
