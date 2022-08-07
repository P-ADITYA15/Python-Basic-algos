print("sun  mon  tue  wed  thu  fri  sat")
c=0
l = [1,2,3,4,5,6,7,8,9]
for i in range(5):
    for j in range(7):
        c+=1
        if c>31:
            break
        if len(str(c))==1:
            print("0"+str(c),end ='   ')
        else:
            print(c,end='   ')
    print()
