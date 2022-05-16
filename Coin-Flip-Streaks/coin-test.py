import random

randomList = []
head = 0
tail = 0

# 投掷 1000 次，看正反面的次数分别是多少。
for i in range(1000):
    randomNum = random.randint(0, 1)
    if randomNum == 0:
        randomList.append("0")
    elif randomNum == 1:
        randomList.append("1")

for i in range(len(randomList)):
    if randomList[i] == '0':
        head += 1
    elif randomList[i] == '1':
        tail += 1

print(head)
print(tail)
