"""Comma Code

Given a list, return all items separated by commas.
"""


def comma_join(arr):
    # join all elements with commas and add "and" at the end
    return ", ".join(arr[:-1]) + " and " + arr[-1]


spam = ["apples", "bananas", "tofu", "cats"]
print(comma_join(spam))
