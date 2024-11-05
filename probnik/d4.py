f=open("26_z_№3.txt")
n=[int(x) for x in f.readlines()]
forpok=sorted(n)
formag=sorted(n, reverse=True)
sum1=0
sum2=0
for i in range(int(2500)):
    sum1+=formag[i]
for i in range(int(2500)):
    sum2+=forpok[i]
print(sum(n)-sum1/2, sum(n)-sum2/2)