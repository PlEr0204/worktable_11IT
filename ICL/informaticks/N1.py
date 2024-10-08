f=open("input.txt")
n=sorted([str(x)[:-1] for x in f.readlines()])
ans={}
for i in range(len(n)):
    if n[i] not in ans:
        ans[n[i]]=1
    else:
        ans[n[i]]+=1
f.close()

f1=open("output.txt", "w")
key=ans.keys()
for i in key:
    k=i+" "+str(ans[i])+"\n"
    f1.write(k)
f1.close()

