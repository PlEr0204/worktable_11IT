def prost(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
            

k=0
for i in range(3000000, 10000000-1):
    if prost(i) and prost (i+2):
        k+=1
        sr=(i+(i+2))/2
print(k, sr)


