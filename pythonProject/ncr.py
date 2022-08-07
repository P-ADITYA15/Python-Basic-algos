#ncr
def fac(n):
    f = 1
    for i in range(n):
        f = f*(i+1)
    return f
n = 5
r = 2
ncr = fac(n)/(fac(r)*fac(n-r))
print(ncr)
