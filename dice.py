import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)

dice = Dice()
print(dice.roll())