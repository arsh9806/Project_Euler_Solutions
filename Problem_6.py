case = int(input())
lis = []
for _ in range(case):
    n = int(input())
    lis.append(((n*(n+1))//2)**2 - (n*(n+1)*(2*n + 1))//6)
for i in lis:
    print(i)