for i in range(100,1000):
    z=i
    sum_ch=0
    pro_ch=1
    while i!=0:
        sum_ch+=i%10
        pro_ch*=i%10
        i=i//10
    if str(pro_ch)+str(sum_ch)==str(24019):
        print(z)
