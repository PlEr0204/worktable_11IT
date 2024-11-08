n=int(input())
A = [list(map(int, input().split())) for i in range(n)]
k=0
for i in range(n):
    print(sum(A[i]))
    