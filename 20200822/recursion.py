num =7

def fact_i(num):
    result = 1
    while num > 0:
        result = result * num
        num -= 1
    return result
def fact_r(num):
    if num == 1 :
        return 1
    else:
        return num * fact_r(num -1)

def fibo_i(num):
    first = 1
    second = 1
    while num > 2:
        hi = second
        second = first + second
        first = hi
        num -= 1
    return second
def fibo_r(num):
    if num == 1 or num == 2 :
        return 1
    else:
        return fibo_r(num-1) + fibo_r(num-2)
userNum = 0
while userNum != -1 :
    userNum = int ( input("Type a number : "))
    # print(fact_i(userNum))
    # print(fact_r(userNum))
    print("Iteration : " + str(fibo_i(userNum)))
    print("Recursion : " + str(fibo_r(userNum)))
