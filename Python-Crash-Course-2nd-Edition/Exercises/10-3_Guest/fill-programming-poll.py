responses = []

while True:
    print("Why do you like programming?")
    response = input()
    responses.append(response)

    print("Would you like let someone else response? (y/n)")
    continue_poll = input()
    if continue_poll != 'y':
        break

with open('programming_poll.txt', 'a') as f:
    for response in responses:
        f.write(f"{response}\n")