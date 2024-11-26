def dfs(u):
    vis[u]= False
    for v in range(n):
        if vis[v] and ma[u][v]!=0:
            dfs(v)
n=int(input())
vis=[True]*n; ma=[]
for i in range(n):
    ma.append(list(map(int,input().split())))
k=0
for u in range(n):
    if vis[u]==True:
        dfs(u)
        k+=1
print(k)

