f=[0]*702
for n in range(1,702):
    if n<=400:
        f[n]=1
    else:
        f[n]=f[n-1]*(n-400)
print(f[701]/f[697])
