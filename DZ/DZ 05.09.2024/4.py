a=[]
for i in range(1325, 15367+1):
    if i%13==0 and i%7!=0 and i%17!=0 and i%19!=0 and i%23!=0:
        a.append(i)
print(len(a), min(a))
