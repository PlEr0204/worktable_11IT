f=open("17_1.txt")
n=[int(x) for x in f.readlines()]
a=[]
for i in range(len(n)):
    if n[i]%100==17:
        a.append(n[i])
k=0
a1=[]
for i in range(len(n)-2):
    if n[i]%5==0 or n[i+1]%5==0 or n[i+2]%5==0:
        k1=0
        for j in range(3):
            if n[i+j]//1000>1 and n[i+j]//1000<10:
                k1+=1
        if k1==2:
            if (n[i]+n[i+1]+n[i+2])>max(a):
                k+=1
                a1.append(n[i]+n[i+1]+n[i+2])
print(k, max(a1))

