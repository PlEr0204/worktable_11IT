f=open("s24.txt")
s=f.readlines()[0]
s=s.replace("RSQ","*")
c=0
ans=0
for i in range(len(s)):
    if s[i]=="*":
        if s[i-1]=="Q" and c==0:
            c+=1
        else:
            if s[i-2]=="S" and s[i-1]=="Q" and c==0:
                c+=2
        c+=3
    elif s[i+1]=="R" and c!=0 and s[i]!="*":
        if s[i+1]=="R" and c!=0:
            c+=1
        else:
            if s[i+1]=="R" and s[i+2]=="S" and c!=0:
                c+=2
    else:
        if c!=0:
            ans=max(c,ans)
            c=0
        else:
            c=0
print(ans)
        