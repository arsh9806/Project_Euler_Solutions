from functools import reduce
case = int(input())

for _ in range(case):
    max = 0
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    number = input()
    for i in range(n-k+1):
        if '0' in number[i:i+k]:
            continue
        else:
            lis = [int(a) for a in number[i:i+k]]
            mul = reduce(lambda a,b : a*b ,lis)
            if mul > max:
                max = mul
    print(max)