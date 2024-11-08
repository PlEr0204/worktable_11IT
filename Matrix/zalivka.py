n=int(input())
x0, y0=map(int,input().split())
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
ymax=len(m)
xmax=len(m[0])
new_color=2
color=m[y0][x0]
Q=[]
Q.append((x0,y0))
while len(Q)>0:
    x, y=Q.pop(0)
    if m[y][x]==color:
        m[y][x]=new_color
        if x>0:
            Q.append((x-1,y))
        if x<xmax-1:
            Q.append((x+1,y))
        if y>0:
            Q.append((x,y-1))
        if y<ymax-1:
            Q.append((x,y+1))
for j in range(n):
    print(*m[j])