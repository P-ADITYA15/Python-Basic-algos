a= [{1:4},{5:3,3:5,1:5},{2:1,4:2}]
c=[]
b=[]
for i in range(len(a)):
    b.append(len(a[i]))
b.sort()
for j in b:
    for k in a:
        if j== len(k):
            c.append(k)
        
print(c)