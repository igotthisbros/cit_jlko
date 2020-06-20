#list
x = [3, 'ball', True, 7, 'f']
print(x)
print(x[0]+x[3])
x[1] = 10
print(x)
x[3] = x[3] + x[1]
print(x)

b = {"age" : 24, "name" : "Elsa", "isMarried" : False}
print(b)
print(b["age"])
b["isMarried"] = True
print(b)

moon = {"lastName" : "Moon", "isMarried" : True, "Nationality" : "SK"}
kim = {"lastName" : "Kim", "isMarried" : False, "Nationality" : "NK"}
trump = {"lastName" : "Trump", "isMarried" : True, "Nationality" : "USA"}

canMarryKimMoon = (not moon["isMarried"]) and (not kim["isMarried"])

print(canMarryKimMoon)
