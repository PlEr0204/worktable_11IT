def prost(n):
    m=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            m.add(i)
            m.add(n//i)
    return sorted(m)
n1=int(input())
ans=prost(n1)
print(*ans, sep=" ")
print(len(ans))