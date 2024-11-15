
fin=open('Graf/matr_dfs.txt')
sm=set()
def dfs(u):
    global sm
    vis[u]= False
    print('in',u+1)
    sm.add(u+1)

    for v in range(n):
        if vis[v] and ma[u][v]==1:
            dfs(v)
    print('out',u+1)

n=int(input('количество вершин графа:'))
u=int(input('номер вершины:'))-1
vis=[True]*n; ma=[]
for i in range(n):
    ma.append(list(map(int,fin.readline().split())))
dfs(u)
print(sm)
if len(sm)==n:
    print("Граф связный")
else:
    print("граф не связный")
    