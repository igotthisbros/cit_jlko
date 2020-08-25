def hanoi(num, frombar, midbar, tobar):
    if num == 1 :
        print("1" + ":" + frombar + "=>" + tobar)
    else :
        hanoi(num -1, frombar, tobar, midbar)
        print(str(num) + " : " + frombar + "=>" + tobar)
        hanoi(num -1, midbar, frombar, tobar)
plates = 8
barFrom = "A"
barMid = "B"
barTo = "C"
hanoi(plates, barFrom, barMid, barTo )
