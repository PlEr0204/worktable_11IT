n, m=map(int,input().split())
A=[[0]*n for i in range(n)]
for i in range(m):
    y0, x0=map(int,input().split())
    A[y0-1][x0-1]=1
for i in range(len(A)):
    print(*A[i])
