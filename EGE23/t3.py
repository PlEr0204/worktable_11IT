
def f(st, k):
    if k==15:
        mn.add(st)
    else:
        f(st+2, k+1)
        f((st*2)+1, k+1)

mn=set()
f(2, 0)
print(len(mn))
