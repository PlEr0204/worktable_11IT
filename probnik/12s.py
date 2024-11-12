"""
for i in range():
    s="1"*i
    while "111" in s:
        s=s.replace("111","2",1)
        s=s.replace("222","11",1)
        s=s.replace("1","2",1)
    print(i, s)
"""
k=0
st=123456794
fn=678901234
for i in range(41,678901234+1,16):
    if st<=i<=fn:
        k+=1
for i in range(10,678901234+1,16):
    if st<=i<=fn:
        k+=1
for i in range(16,678901234+1,16):
    if st<=i<=fn:
        k+=1
print(k)