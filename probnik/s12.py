k=0
for i in range(234567900, 789012345+1):
    s="1"*i
    while "111" in s:
        s.replace("111","2",1)
        s.replace("222","11",1)
        s.replace("1","2",1)
    if len(s)==3:
        k+=1
        print(k)