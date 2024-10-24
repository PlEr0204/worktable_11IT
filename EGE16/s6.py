f=[0]*48
f[0]=0
f[1]=1
f[2]=1
for n in range(3,48):
    f[n]=f[n-2]+f[n-1]
print(f[47])