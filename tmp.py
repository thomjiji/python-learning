import random

random.seed(1000)

for i in range(5):
    print('{:.3f}'.format(random.random()), end=' ')
print()