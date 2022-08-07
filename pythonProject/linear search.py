
#linear search
lst = [2,3,1,6]
n = int(input("enter the element which u want to find: "))
a= False
for i in range(len(lst)):
    if lst[i]==n:
        print(i)
        a = True
if not a:
    print("element not present")
