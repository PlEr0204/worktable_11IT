def f(n):
    try:
        if n<2:
            return 1
        if n>=2 and n%3==0:
            return f(n/3)-1
        if n>=2 and n%3!=0:
            return f(n-1)+17
    except:
        pass
k=0
for n in range(1,100001):
    st=f(n)
    if st!=None and st==43:
        k+=1
print(k)