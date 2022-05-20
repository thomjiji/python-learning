from random import choice


def make_random_ticket(possibilities):
    random_ticket = []
    while len(random_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in random_ticket:
            random_ticket.append(pulled_item)
    return random_ticket


def check_winning(my_ticket, winning_ticket):
    """
    Check whether every item in my_ticket is in winning_ticket.
    Return False even if only one item is not in winning_ticket.
    """
    for item in my_ticket:
        if item not in winning_ticket:
            return False

    return True


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = make_random_ticket(possibilities)

tries = 0
won = False

while not won:
    my_ticket = make_random_ticket(possibilities)
    won = check_winning(my_ticket, winning_ticket)
    tries += 1
    if tries >= 10_000:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {tries} tries to win!")
else:
    print(f"Tried {tries} times, without pulling a winner. :(")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")