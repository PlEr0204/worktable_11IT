f=[0]*2029
f[1]=1
f[2]=1
f[3]=1
for n in range(4,2029):
    f[n]=(n+3)*f[n-2]
print(f[2028]/f[2024])
