f=open("EGE/26_p.txt")
n=int(f.readline())
m=[list(map(int,f.readline().split())) for i in range(n)]
m.sort(key=lambda x: x[1])
for i in range(5):
    print(m[i])
res=[m[0][1]]
for st,fn in m:
    if st>=res[-1]:
        res.append(fn)
mx_st=max(m)[0]
pauza=mx_st-res[-2]
print(len(res),pauza)