""" The Collatz Sequence

The given number always converges to 1.
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

# prompt the user for an integer
num = int(input("Enter number: "))

# continue calling collatz until result is 1
while True:
    num = collatz(num)
    if num == 1:
        break
