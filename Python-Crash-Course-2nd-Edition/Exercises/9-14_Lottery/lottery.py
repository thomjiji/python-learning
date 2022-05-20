import random

lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           'a', 'b', 'c', 'd', 'e']

lucky_num_list = []
i = 0
while i < 5:
    lucky_num_list.append(random.choice(lottery))
    i += 1

lucky_num = ', '.join(lucky_num_list)
print(f"Anyone who has {lucky_num} wins the price!")