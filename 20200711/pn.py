# n = 2345
# while n/n - 1 > 1 :
n = 2


while n < 1000:
    divisor = 2
    count = 0
    while divisor < n:
        if n % divisor == 0:
            count = count + 1
        divisor = divisor + 1

    if count == 0:
        print(n)

    n = n + 1
