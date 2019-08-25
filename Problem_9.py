case = int(input())
for _ in range(case):
    max = -1
    n = int(input())
    for a in range(1,n//3 +1):
        b = (n**2 - 2*a*n)//(2*n - 2*a)
        c = n - a - b
        if (a**2 + b**2 == c**2):
            mul = a*b*c
            if mul > max:
                max = mul

    print(max)