a = {1:"demon slayer",2:"attack on titan",3:"shinchan",4:"no game no life",5:"classroom of elite"}
print(a)
b = int(input("select the movie: "))
print("you've selected",a[b])
print("how many seats do u want to book")
c = int(input("enter no of seats: "))
d = [[1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10]]
amt =0
for i in d:
    print(i)
print()
print("      S C R E E N  \n")
print("please select the seats")
while c>0:
    e = int(input("enter row no.: "))
    f= int(input("enter seat no.: "))
    print("you have successfully booked, row:",e,"seat no.",d[e-1][f-1])
    c-=1
    if e==1:
        amt+=500
    elif e==2:
        amt+=400
    elif e==3:
        amt+=300
    elif e==4:
        amt+=200


print("your total amount is",amt)
