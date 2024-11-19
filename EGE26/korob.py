f=open("26.txt")
kont=list(x for x in f)
m=[]
for x in kont:
    r=x
    r=int(r)
    if r%2==0:
        col="S"
    else:
        col="K"
    m.append([r,col])
m.sort(reverse=True)
sklad=[]
while len(m)>0:
    b=[m.pop(0)]
    for i in range(len(m)):
        if m[i][1]!=b[-1][1]:
            if b[-1][0]-m[i][0]>=7:
                b.append(m[i])
                m[i]="*"
    m=list(x for x in m if x!="*")
    sklad.append(len(b))
print(max(sklad))

