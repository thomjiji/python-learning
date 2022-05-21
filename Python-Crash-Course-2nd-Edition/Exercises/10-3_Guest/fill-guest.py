print("Please enter your name: ")
name = input()
with open('guest.txt', 'a') as guest_list:
    guest_list.write(name + '\n')