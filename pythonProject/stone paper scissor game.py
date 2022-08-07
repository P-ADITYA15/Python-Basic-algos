import random
print("Score 3 to win ")
c =0
d=0
index = {0:'stone',1:'paper',2:'scissior'}
li = [[0,-1,1],[1,0,-1],[-1,1,0]]
lst=[]
lst1=[]
for i in index.keys():
    lst.append(i)
for j in index.values():
    lst1.append(j)
for z in range(25):
    print("\n")
    print(index)
    n = int(input("enter the key associated with the value: "))
    a = random.choice(lst)
    b = li[n][a]
    print("computer had chosen",lst1[a])
    if b == 0:
        pass
    elif b == 1:
        c += 1
    else:
        d += 1
    print("user score: ",c,",computer score: ",d)
    if c == 3:
        print("\n\tYOU WON")
        break
    elif d == 3:
        print("\n\tYOU LOST")
        break
