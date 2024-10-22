'''
def f(n):
    if n<10:
        return n
    else:
        return f(g(n))
def g(n):
    if n<10:
        return f(n)
    else:
        return g(n%10)+g(n//10)
ans=[]
for i in range(100000000):
    ans.append(f(i))
print(ans)
'''
k=0
for i in range(100000000, 200000001, 9):
    k+=1
print(k)
