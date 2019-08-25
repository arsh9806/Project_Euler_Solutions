case = int(input())
lis = []
for _ in range(case):
    n = int(input())
    a = 1
    b = 2
    c = a + b
    sum1 = 2
    while True:

        if c < n and c % 2 == 0:
            sum1 += c

        a = b
        b = c
        c = a + b
        if c < n:
            continue
        else:
            break
    lis.append(sum1)
for i in lis:
    print(i)