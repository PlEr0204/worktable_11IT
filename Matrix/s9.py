n=int(input())
A = [list(map(int, input().split())) for i in range(n)]
k=0
s=0
for i in range(n):
    for j in range(n):
        if i<j and A[i][j]==1:
            if A[i][j]==A[j][i]:
                k+=1
            s+=1
if k==s:
    print("YES")
else:
    print("NO")