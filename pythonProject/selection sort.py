#selection sort
l = [2,2,3,1,8]
for i in range(len(l)-1):
    mi = i
    for j in range(i,len(l)):
        if l[j]<l[mi]:
            mi = j
    l[i],l[mi]=l[mi],l[i]
print(l)