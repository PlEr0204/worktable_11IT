#####ввод
f=open("input.txt")
n1=[str(x)[:] for x in f.readlines()]
n=[]
for i in range(len(n1)):
    print(n1[i])
    s=n1[i].replace("!", " ")
    s=n1[i].replace("?", " ")
    s=n1[i].replace(":", " ")
    s=n1[i].replace(";", " ")
    s=n1[i].replace(",", " ")
    s=n1[i].replace(".", " ")
    s=s.lower()
    print(s)
    s1=s.split()
    print(s1)
    for j in range(len(s1)):
        n.append(s1[j])
n=sorted(n)
###############сама прога
ans={}
for i in range(len(n)):
    if n[i] not in ans:
        ans[n[i]]=1
    else:
        ans[n[i]]+=1
f.close()
##############сортировка по значения по убыванию словаря
ans1 = dict(sorted(ans.items(), key=lambda item: -item[1]))
###############вывод в файл
f1=open("output.txt", "w")
key=ans1.keys()
for i in key:
    k=i+" "+str(ans1[i])+"\n"
    f1.write(k)
f1.close()
