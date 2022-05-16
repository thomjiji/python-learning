try:

    def collatz(number):
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1


    inputNum = int(input("Please enter a number: "))
    iteration: int = 0

    while True:
        inputNum = collatz(inputNum)
        iteration += 1
        print(inputNum, end=", ")
        if inputNum == 1:
            break

    print("Number of iteration:", iteration)

except ValueError:
    print("Please enter an integer.")
