lst = [[1,2,3],[0,0,1],[0,0,0]]
c=0
for i in range(len(lst)):
    for j in lst[i]:
        if j==0:
            c+=1
if c>((len(lst)*len(lst[0]))-c):
    print("it is a sparse")
else:
    print("it is not a sparse")


