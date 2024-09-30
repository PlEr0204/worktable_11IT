a="Съешь ещё этих мягких французских булок"
for i in range(len(m)):
        if m[i] not in ans:
            ans[m[i]]=1
        else: 
            ans[m[i]]+=1
