while True:
    name = input("Please enter your name: (If you don't want to, enter quit instead.)")
    if not name == 'quit':
        print(f"Welcome! {name}.")
        with open('guest_book.txt', 'a') as guest_book:
            guest_book.write(f"{name}\n")
        break
    elif name == 'quit':
        print("OK, see you in next life.")
        break