#matrix multiplication
a = [[2,3,4],
     [3,4,5],
     [4,2,2]]
b = [[2,3,4,3],
     [3,4,5,2],
     [4,2,2,1]]
c = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
for r in c:
    print(r)
