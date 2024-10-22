f=[0]*9995
for n in range(0,9995):
    if n%2==0:
        f[n]=f[n+2]-3
    else:
        f[n+2]+1
print((f[2024] + 3*f[2023]) / f[2022])