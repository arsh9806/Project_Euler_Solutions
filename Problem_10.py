#using Seive's Method
def find_sum(num):
    sum1 = 0
    numbers = [True]*(num+1)
    primes = [0] * (num+1)
    numbers[0] = numbers[1] = False

    for i,is_prime in enumerate(numbers):

        if is_prime:
            sum1 += i

            for j in range(i*i,num + 1,i):
                numbers[j] = False
        primes[i] = sum1
    return primes
sumlis = find_sum(1000000)#list of summation of primes upto that index
case = int(input())
for _ in range(case):
    index = int(input())
    print(sumlis[index])