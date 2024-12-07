def f(a,m):
    if a <= 19:
        return m%2==0
    if m==0:
        return False
    h=[f(a-2,m-1), f(a-5,m-1), f(a//3,m-1)]
    return any(h) if (m+1)%2==0 else all(h)
for s in range(100,19,-1):
    for m in range(5):
        #если Петя 1м ходом, то m=1
        #если Ваня 1м ходом то m=2
        #.....
        if f(s,m):
            if m==4:
                print(s,m)
            break
