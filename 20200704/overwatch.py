rating = -300
if(0 < rating < 1500):
    print("Bronze")
elif(rating < 0 or rating > 5000):
    print("Error")
elif(1500 < rating < 2000):
    print("Silver")
elif(2000 < rating < 2500):
    print("Gold")
elif(2500 < rating < 3000):
    print("Platinum")
elif(3000 < rating < 3500):
    print("Diamond")
elif(3500 < rating < 4000):
    print("Master")

else :
    print("Grand Master")

rating = 1800

if rating < 0 or rating > 5000 :
    print("Error")
elif rating > 4000 :
    print("GM")
elif rating > 3500 :
    print("M")
elif rating > 3000 :
    print("D")
elif rating > 2500 :
    print("P")
else :
    print("BSG")
