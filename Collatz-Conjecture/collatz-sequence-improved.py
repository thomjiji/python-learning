try:

    def collatz(number):
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1


    inputNum = int(input("Please enter a number: "))
    iteration: int = 0
    newline: int = 1

    while inputNum != 1:
        inputNum = collatz(inputNum)
        iteration += 1
        if iteration == 10 * newline or inputNum == 1:
            print(inputNum)
            newline += 1
        else:
            print(inputNum, end=", ")

    print("Number of iteration:", iteration)

except ValueError:
    print("Please enter an integer.")
