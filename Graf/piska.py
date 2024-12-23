#алгоритм остовного дерева
N, M=map(int,input().split())
W=[[0]*N for i in range(N)]
for i in range(M):
    i1, j1, dist1=map(int,input().split())
    W[i1-1][j1-1]=dist1
#леха дуралей
col=[i for i in range(N)] #цвета твоей жопы, надо короче
ostov=[]
Sum_ostov=0
for k in range(N-1):
    minDist=100000000000000000000000000000000000000000000000000000000000000
    for i in range(N-1):
        for j in range(i+1,N):
            if col[i]!=col[j]  and W[i][j]!=0 and W[i][j]<minDist:
                iMin=i
                jMin=j
                minDist=W[i][j]
    ostov.append((iMin,jMin))
    c=col[jMin]
    for i in range(N):
        if col[i]==c:
            col[i]=col[iMin]
for edge in ostov:
    Sum_ostov+=W[edge[0]][edge[1]]
    print("(",edge[0],",",edge[1],")")
print(str(Sum_ostov)+" ",end=" ")
for edge in ostov:
    print("(",edge[0],edge[1],")",end=" ")