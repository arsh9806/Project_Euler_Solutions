from math import gcd
case = int(input())
lis = []
for _ in range(case):
    N = int(input())
    a = 1
    b = 2
    while b<=N:
        a = (a*b)//gcd(a,b)
        b += 1
    lis.append(a)
for i in lis:
    print(i)