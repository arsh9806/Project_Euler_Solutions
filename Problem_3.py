lis = []
case = int(input())
for _ in range(case):
    number = int(input())
    B = 2
    while number > B:
        if number % B == 0:
            number //= B
            B = 2
        else:
            B += 1
    lis.append(B)
for i in lis:
    print(i)