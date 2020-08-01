
def identifier(num):
    digit = 1
    clap = 0
    while 10 ** (digit -1) < num:
        digitNum = (num% (10 ** digit) - num % (10 ** (digit -1)))/ 10 ** (digit -1)
        if (digitNum % 3 == 0 and digitNum != 0):
            clap = clap + 1
        digit = digit + 1
    if (clap ==0):
        return {"type" : "num", "value" : num}
    else :
        claps = ""
        while clap >0 :
            claps = claps + "clap"
            clap = clap -1
        return {"type" : "clap", "value" : claps}

print("#### WELCOME TO 369 GAME ####")
computers = int(input("Type the number of computers : "))
gameover = False
number = 1
while not gameover :
    computerTurn = computers
    while computerTurn > 0:
        print (identifier(number)["value"])
        computerTurn -= 1
        number += 1
    userInput = input("Your Turn : ")
    answer = identifier(number)
    if answer ["type"] == "num" and int(userInput) != answer ["value"]:
        gameover = True
    elif answer ["type"] == "clap" and (userInput) != answer ["value"]:
        gameover = True
    else :
        number += 1

print("#### GAME OVER ####")
# playing = True
#
# while playing :
#     userNum = int ( input("type a number : "))
#     if (userNum == -1):
#         playing = False
#     else :
#         print( identifier(userNum))
#
# print("Game Over")
    # if userNum%10 == 3 or 6 or 9:
    #     return("clap")
    # elif (userNum%100 - userNum%10)/10 == 3 or 6 or 9:
    #     return("clap")
    # elif (userNum%1000 - userNum%100)/100 == 3 or 6 or 9:
    #     return("clap")
    # else:
    #     return(userNum)
