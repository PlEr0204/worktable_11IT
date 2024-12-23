n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
s, f = map(int, input().split())
def bfs(n,a,f,s):
    vis = [False]*n
    d=[-1]*n
    p=[-1]*n
    s -= 1
    f -= 1
    q = [s]
    vis[s]=True
    d[s]=0
    while q:
        ver=q.pop(0)
        for i in range(n):
            if a[ver][i]==1 and not vis[i]:
                q.append(i)
                vis[i]=True
                d[i]=d[ver]+1
                p[i]=ver
    path=[f+1]
    k=f
    while p[k]!=-1:
        path.append(p[k]+1)
        k=p[k]
    return path
print(bfs(n,a,f,s))