class Food:
    # calories = 100 #property
    # taste = "Good"
    # price = 100000
    def __init__(self, cal, tst, prc):
        self.calories = cal
        self.taste = tst
        self.price = prc
    def myTaste(asd): #method
        print("I taste " + asd.taste)

class KoreanFood(Food):
    def __init__(self, cal, tst, prc, scv):
        Food.__init__(self, cal, tst, prc)
        self.scoville = scv
class FrenchFood(Food):
    def __init__(self, cal, tst, prc, wne):
        super().__init__(cal, tst, prc)
        self.wine = wne
    def tasteWine(self, vintage):
        print("this tastes like" + self.wine + " of " + str(vintage))
# f1 = Food()
# f2 = Food()
# f2.calories = 200
# f2.taste = "bad"
f1 = Food(250, "Awesome", 30000)
f2 = Food(177, "Gross", 5300)
f3 = KoreanFood(100, "Not bad", 4000, 300)
f4 = FrenchFood(100, "Fantastic", 30000, "Mutong")
f3.myTaste()
f4.tasteWine(1989)
print(f3.scoville)
print(f1.calories)
print(f2.calories)
f2.myTaste()
print(f2.price)
