# variables = (1,1,2,3,5,8,13)


first = 1
second = 1

while second < 100000:
    olaf = first
    first = second
    second = olaf + second
    print(second)
