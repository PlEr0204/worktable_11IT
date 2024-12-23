f=open("s9.csv")
k=0
for s in f:
    m=[int(x) for x in s.split(";")]
    mp=[x for x in m if m.count(x)==2]
    mn=[x for x in m if m.count(x)==1]
    if len(set(mp))==3:
        if (max(mp)+min(mp))/2 < max(mn):
            k+=1
print(k)