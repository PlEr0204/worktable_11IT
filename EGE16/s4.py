def f(n):
    try:
        if n==0:
            return 0
        if n>0 and n%2==0:
            return f(n/2)
        if n>0 and n%2!=0:
            return f(n-1)+3
    except:
        pass
k=0
for n in range(1,1001):
    st=f(n)
    if st!=None and st==18:
        k+=1
print(k)