def path(f):
    if f==s:
        print(s+1,end=' ')
        return
    path(p[f])
    print(f+1,end=' ')
n, s, f=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
p=[0]*n; inf=1e10; d=[inf]*n; vis=[False]*n
s-=1;f-=1; d[s]=0
for i in range(n):
    mi=inf
    for j in range(n):
        if not vis[j] and d[j]<mi :
            mi=d[j]
            kmi=j
    if mi==inf: break
    vis[kmi]=True
    for j in range(n):
        if a[kmi][j]!=0 and not vis[j] and d[kmi]+a[kmi][j]<d[j]:
            d[j]=d[kmi]+a[kmi][j]
            p[j]=kmi
if d[f]>=inf:
    print(-1)
else:
    path (f)