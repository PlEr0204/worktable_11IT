n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
vis = [-1]*n
s=0
q = [s]
vis[s]=0
while q:
    ver=q.pop(0)
    for i in range(n):
        if a[ver][i]==1 and vis[i]==-1:
            q.append(i)
            vis[i]=vis[ver]+1
k=0
for i in range(len(vis)):
    if vis[i]==0:
        k+=1
print(k)
