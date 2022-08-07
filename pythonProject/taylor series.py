# taylor series
from math import *

x = float(input("enter angle in degree: "))
n = int(input("how many terms: "))
s = 0
a = x * (pi / 180)
for i in range(n):
    sign = pow(-1, i)
    s = s + (sign * (a ** (2 * i + 1)) / factorial(2 * i + 1))

print(s)

