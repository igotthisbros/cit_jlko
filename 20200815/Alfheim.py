print("Welcome to Alfheim! The land of elves!")
name = input("What is your name ? : ")
conv1 = input("Welcome, " + name +". I'm Titania, your guide to this world. Press enter to continue")
if conv1 ==(" "):
    True
else: True

conv2 = input("Watch out "+name+"! Bunch of Teemos suddenly appeared!")
if conv2 ==(" "):
    True
else: True
conv3 = input("Choose your weapon to fight the Teemos!")
if conv3 ==(" "):
    True
else: True
weapon =  input("You can choose a sword, a staff, or a bow : ")
if weapon == ("sword"):
    job = ("Swordsman")
    print("you are now a swordsman !")
if weapon == ("staff"):
    job = ("Wizard")
    print("you are now a wizard !")
if weapon == ("bow"):
    job = ("Archer")
    print("you are now an archer !")

level = 1
exp = 0

print("User Info : " + name + " / " + job +  " /Lv" +str(level) +  " / " + str(exp) + " exp" )
conv4 = input("Now let's go to the dungeon to stack some exps! ")
if conv4 == (" "):
     True
else:
     True
conv5 = input("You've arrived at dungeon! ")
if conv5 ==(" "):
    True
else: True
conv6 = input("You've encountered a wild Teemo! Take out your " + weapon + "!")
if conv6 ==(" "):
    True
else: True
def teemoDies (c):
    teemoHealth = 500

    while (teemoHealth > c):
        conv7 = input ( "It's still alive ! say slash again ! :")
    else :
        return "dead"
command_sl = input("say slash to kill teemo! : ")

if command_sl == "slash" :
    damage = 600
else:
    damage = 0
print(teemoDies(damage))
exp = 500
command = input("you've gained exps! type in check status to know your character info! : ")
while command != "check status":
    command =input("Try again.. : ")
print("User Info : " + name + " / " + job +  " /Lv" +str(level) +  " / " + str(exp) + " exp")
