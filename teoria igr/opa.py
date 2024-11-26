def f(a,b,m):
    if a+b >= 136:
        return m%2==0
    if m==0:
        return False
    h=[f(a+2,b,m-1), f(a*3,b,m-1), f(a,b+2,m-1), f(a,b*3,m-1)]
    return any(h) if (m+1)%2==0 else all(h)
for s in range(1,133):
    for m in range(5):
        #если Петя 1м ходом, то m=1
        #если Ваня 1м ходом то m=2
        #.....
        if f(s,2,m):
            if m==1:
                print(s,m)
            break
print("всё")
