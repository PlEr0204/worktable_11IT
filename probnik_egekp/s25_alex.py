for i in "0123456789":
    for x in range(0,100):
        for a in "0123456789":
            for b in "0123456789":
                s="12"+i+"3"+str(x)+"456"+a+b+"9"
                if int(s)%98591==0:
                    print(s,int(s)/98591)