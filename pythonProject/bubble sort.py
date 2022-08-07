#bubble sort
l = [-2,4,1,76,-2]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j+1],l[j]=l[j],l[j+1]
print(l)