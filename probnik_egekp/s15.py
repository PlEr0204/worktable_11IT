for A in range(1,200):
    f=True
    for x in range(1,2000):
        if not((x&A==0) or (not(x&37==0)) or (not(x&12==0))):
            f=False
    if f:
        print(A)
