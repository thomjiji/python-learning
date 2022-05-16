import random

numberOfStreaks = 0
streak = 0
randomList = []

for experimentNumber in range(10000):
    for i in range(100):
        randomNum = random.randint(0, 1)
        if randomNum == 0:
            randomList.append("0")
        elif randomNum == 1:
            randomList.append("1")

    for i in range(len(randomList)):
        if i == 0:
            pass
        elif randomList[i] == randomList[i - 1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1
            streak = 0

    randomList = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
# print(numberOfStreaks)
