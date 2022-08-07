#pascal triangle
def fac(x):
    fact =1
    for i in range(x):
        fact=fact*(i+1)
    return fact
n = 5
for i in range(n):
    print("  "*(n-i),end='')
    for j in range(i+1):
        print(fac(i)//(fac(j)*fac(i-j)),end='    ')
    print()
