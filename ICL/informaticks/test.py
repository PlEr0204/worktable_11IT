rooms = {"Pink": "Rm 403", "Space": "Rm 201", "Quail": "Rm 500", "Lime": "Rm 503"}
#1
print(*rooms)

#2
print(sorted(rooms))

#3
m = sorted(rooms.items())
print(rooms.items()) # Превращение в массив кортежей
print(m)

#4
v = dict(m) 
print(v)

#5
s1_rooms = dict(sorted(rooms.items(), key=lambda item: item[1]))
print(s1_rooms)

#6
s2_rooms = dict(sorted(rooms.items(), key=lambda item: item[0]))
print(s2_rooms)

#7
m1 = rooms.setdefault("Pink")
print(m1)
print(rooms)

m1 = rooms.setdefault("Solo")
print(m1)
print(rooms)

rooms2 = {"Pink": 17, "Space": 4, "Quail": 51, "Lime": 30, "Lama": 30}
#8
s1_rooms2 = dict(sorted(rooms2.items(), key=lambda item: -item[1]))
print(s1_rooms2)

#9
s2_rooms2 = dict(sorted(rooms2.items(), key=lambda item:( item[1], item[0])))
print(s2_rooms2)