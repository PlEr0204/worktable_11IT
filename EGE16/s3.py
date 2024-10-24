def f(n):
    try:
        if n<=5:
            return n
        if n>5 and n%3==0:
            return n+f(n/3+2)
        if n>5 and n%3!=0:
            return n+f(n+3)
    except:
        pass
for i in range(10000):
    st=f(i)
    if st!=None and st>1000:
        print(i)
        break
