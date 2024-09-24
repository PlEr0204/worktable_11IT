a=[]
for i in range(-9563, -3102-1):
    if i%7==0 and i%11!=0 and i%23!=0:
        if (i*(-1))%10!=8:
            a.append(i)
print(len(a), max(a))