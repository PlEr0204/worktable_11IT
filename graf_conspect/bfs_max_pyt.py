n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
vis = [-1]*n
s, f = map(int, input().split())
s -= 1
f -= 1
q = [s]
vis[s]=0
while q:
    ver=q.pop(0)
    for i in range(n):
        if a[ver][i]==1 and vis[i]==-1:
            q.append(i)
            vis[i]=vis[ver]+1
print(vis[f])
