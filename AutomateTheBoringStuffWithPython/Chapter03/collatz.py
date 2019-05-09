"""The Collatz Sequence

Converge the given number to 1.
"""


def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        print(3 * num + 1)
        return 3 * num + 1


num = int(input("Enter number: "))

# call collatz until result is 1
while True:
    num = collatz(num)
    if num == 1:
        break
