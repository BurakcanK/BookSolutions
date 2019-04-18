"""The Collatz Sequence with Input Validation

Converge the given number to 1.
"""

def collatz(num):
    # if the num is even, divide it by two
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    # else multiply it with 3 and add 1
    else:
        print(3 * num + 1)
        return 3 * num + 1

try:
    # prompt the user for an integer
    num = int(input("Enter number: "))

    # continue calling collatz until result is 1
    while True:
        num = collatz(num)
        if num == 1:
            break
except ValueError:
    # in case of invalid input
    print("Input must be an integer.")
