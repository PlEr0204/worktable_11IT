sm=set()
def dfs(u):
    global sm
    vis[u]= False
    sm.add(u+1)
    for v in range(n):
        if vis[v] and ma[u][v]!=0:
            dfs(v)
n=int(input())
vis=[True]*n; ma=[]
for i in range(n):
    ma.append(list(map(int,input().split())))
sm_max=-1
for u in range(n):
    dfs(u)
    if len(sm)>sm_max:
        sm_max=len(sm)
    sm=set()
print(n-sm_max)
