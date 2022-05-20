import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


side_of_6_die = Die(sides=6)
i = 0
while i < 10:
    side_of_6_die.roll_die()
    i += 1

# side_of_10_die = Die(sides=10)
# side_of_10_die.roll_die()