sm=set()
def dfs(u):
    global sm
    vis[u]= False
    sm.add(u+1)
    for v in range(n):
        if vis[v] and ma[u][v]==1:
            dfs(v)
n=int(input())
u=0
vis=[True]*n; ma=[]
for i in range(n):
    ma.append(list(map(int,input().split())))
dfs(u)
if len(sm)==n:
    print("YES")
else:
    print("NO")   