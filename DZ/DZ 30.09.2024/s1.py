dict_country = {}
for i in range(10):
    s1, s2 = input().split(":")
    dict_country[s1] = s2        
dict_country["Austria"]="Vienna" 
dict_country["Russia"]="Moscow"
del dict_country["Bahamas"] 
    
print(*dict_country)
