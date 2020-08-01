
def typeAnswer():
    mode = "typing"
    answer = []
    while mode == "typing":
        print("sdg")
        letter = input("Type letter : ")
        if letter != '':
            mode = "finished"
        else :
            answer[index] = letter
            index = index + 1
    return answer
answer = typeAnswer()
