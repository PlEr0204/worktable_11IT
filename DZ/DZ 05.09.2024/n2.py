def prost(n):
    a=[]
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if n//i==i:
                a.append(i)
            else:
                a.append(i)
                a.append(n//i)
    return a
            


for i in range(135790, 163229):
    a=prost(i)
    if sum(a)>460000:
        print("Число:", i, "Кол-во делителей:",len(a), "Cумма:", sum(a))

