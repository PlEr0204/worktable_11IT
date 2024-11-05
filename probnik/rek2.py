f=[0]*2026
f[1]=1
f[2]=2
for n in range(3,10):
    f[n]=f[n-1]*f[n-2]
#print((f[2025]-f[2023])/f[2021])
for i in range(11):
    print(f[i])
    
