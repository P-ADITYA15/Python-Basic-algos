#binary search
lst = [2,5,8,42,56,77]                        #for binary search list should be sorted before
l = 0
u =len(lst)-1
n = int(input("enter element u want to find: "))
while l<=u:
    mid = (l+u)//2
    if lst[mid]==n:
        print(mid)
        break
    else:
        if lst[mid]<n:
            l = mid+1
        else:
            u = mid-1
else:
    print("not present")
