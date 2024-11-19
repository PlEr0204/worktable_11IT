sm=set()
def dfs(u):
    global sm
    vis[u]= False
    sm.add(u+1)
    for v in range(n):
        if vis[v] and ma[u][v]==1:
            dfs(v)
n, nach=map(int,input().split())
vis=[True]*n; ma=[]
for i in range(n):
    ma.append(list(map(int,input().split())))
ans=[]
for u in range(n):
    sm=set()
    dfs(u)
    if nach in sm:
        ans.append(len(sm))
print(max(ans))
