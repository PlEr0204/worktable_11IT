n=int(input())
A = [list(map(int, input().split())) for i in range(n)]
k=0
sumO=0
for i in range(n):
    sumO+=sum(A[i])
print(sumO//2)