"""
Reference:
1. https://ehmatthes.github.io/pcc_2e/solutions/chapter_9/#9-15-lottery-analysis
2. https://www.omnicalculator.com/statistics/lottery
"""

import random

possibilities = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'a', 'b', 'c', 'd', 'e']

winning_ticket = []

print("let's see what the winning ticket is...")

for i in range(4):
    selected = random.choice(possibilities)
    winning_ticket.append(selected)
    print(f"We pulled a {selected}!")

winning_ticket_str = ' '.join(winning_ticket)
print(f"The final winning ticket is: {winning_ticket_str}.")