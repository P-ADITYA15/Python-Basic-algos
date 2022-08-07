a = [(2,3),(-2,6),(-3,-4),(7,-8),(4,5)]
for i in range(len(a)):
    c=0
    for j in a[i]:
        if j>0:
            c+=1
        if c==len(a[i]):
            print("tuple at position",i,"has positive ele")


