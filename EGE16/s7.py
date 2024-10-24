f=[0]*2024
f[1]=1
for n in range(2,2024):
    f[n]=n*f[n-2]
print(f[2023]/f[2019])