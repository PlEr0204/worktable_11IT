N=int(input())
W=[list(map(int, input().split())) for i in range(N)]
col=[i for i in range(N)]
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
print("Сумма остовного дерева:",Sum_ostov)
