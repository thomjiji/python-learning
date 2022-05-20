import random

lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           'a', 'b', 'c', 'd', 'e']
my_ticket = ['3', '2', 'e', 'b', '3']

# Make an empty list for looping.
wins_num_list = []

# main loop for filling that empty list "wins_num_list"
flag = 0
while flag < 100:
    runs_num = 0
    while runs_num < 5:
        wins_num_list.append(random.choice(lottery))
        runs_num += 1

    if wins_num_list == my_ticket:
        print("You win!")
        flag = 100
    else:
        flag += 1
        wins_num_list = []
        continue
