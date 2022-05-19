import random

numberOfStreaks = 0
CoinFlip = []
streak = 0

# From https://stackoverflow.com/a/60660999
for experimentNumber in range(10000):
    for i in range(100):
        CoinFlip.append(random.randint(0, 1))

    for i in range(len(CoinFlip)):
        if i == 0:
            pass
        elif CoinFlip[i] == CoinFlip[i - 1]:  # checks if current list item is the same as before
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1

    CoinFlip = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
# print(numberOfStreaks)
