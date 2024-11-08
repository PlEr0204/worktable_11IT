n=int(input())
A = [list(map(int, input().split())) for i in range(n)]
k=0
for i in range(n):
    for j in range(n):
        if i==j:
            if A[i][j]==1:
                k+=1
if k>0:
    print("YES")
else:
    print("NO")
