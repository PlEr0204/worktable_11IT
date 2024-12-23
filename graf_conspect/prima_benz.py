"""В стране N городов, некоторые из которых соединены между собой дорогами. Для того, чтобы проехать по одной дороге, 
требуется один бак бензина. В каждом городе бак бензина имеет разную стоимость. Вам требуется добраться из первого города 
в N-ый, потратив как можно меньшее денег. Покупать бензин впрок нельзя.

Входные данные
В первой строке вводится число N (1≤N≤100), в следующей строке идет N чисел, i-ое из которых задает стоимость бензина в 
i-ом городе (всё это целые числа из диапазона от 0 до 100). Затем идет число M – количество дорог в стране, далее идет 
описание самих дорог. Каждая дорога задается двумя числами – номерами городов, которые она соединяет. Все дороги двухсторонние 
(то есть по ним можно ездить как в одну, так и в другую сторону), 
между двумя городами всегда существует не более одной дороги, не существует дорог, ведущих из города в себя."""
n=int(input())
benz=list(map(int,input().split()))
n1=int(input())
nado=[[0]*n for i in range(n)]
for k1 in range(n1):
    l1, l2=map(int,input().split())
    nado[l1-1][l2-1]=1
    nado[l2-1][l1-1]=1
w=[[-1]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if nado[i][j]==1:
            w[i][j]=benz[i]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
start=1
f=n
start -= 1; f -= 1
INF = 10 ** 10
for i in range(n):
    for j in range(n):
        if w[i][j]==-1:
            w[i][j]=INF
dist = [INF] * n
dist[start] = 0
used = [False] * n
min_dist = 0
min_vertex = start
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in range(n):
        if dist[i] + w[i][j] < dist[j]:
            dist[j] = dist[i] + w[i][j]
    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j
if dist[f] != 10**10:
    print(dist[f])
else:
    print(-1)