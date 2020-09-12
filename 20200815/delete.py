 8print("Welcome to Alfheim! The land of elves!")
name = input("What is your name ? : ")
conv1 = input("Welcome, " + name +". I'm Titania, your guide to this world. Press enter to continue")
if conv1 ==(" "):
    True
else: True

conv2 = input("Watch out "+name+"! Bunch of Teemos suddenly appeared!")
if conv2 ==(" "):
    True
else: True


def main():


class Character:
    """ A main protagonist and set of features associated with him/her """
    def __init__(self, name: str, age: int, race: str):
        self.age = age
        self.race = race
        self.weapon_dict = {
            "sword": 10,
            "staff": 30,
            "bow": 5,
        }
    def define_name(self, name):
        self.name = name

    def weaponize(self, weapon: "str"):
        self.attack = self.weapon_dict[weapon]

Aragorn = Character('Aragorn', 54, 'Human')
Gandalf = Character('Gandalf', 99, 'Wizard')


def fight(ally: Character, enemy: Character):
    ally.weaponize("sword")
    enemy.weapon_dict("bow")
    if ally.attack > enemy.attack:
        return "Victory"
    else:
        return "Death"
