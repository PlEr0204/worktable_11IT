def f(n):
    s=bin(n)[2:]
    if n%2==0:
        s=s+s[-2]+s[-1]
    else:
        s="1"+s+"0"
    return int(s,2)
for i in range(1,600):
    if f(i)<100:
        print(i)
