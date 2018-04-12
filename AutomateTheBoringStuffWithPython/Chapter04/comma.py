""" Comma Code

Given a list, returns all items separated by commas.
"""

def commaJoin(arr):
    # join all elements with commas and add 'and' at the end
    return ', '.join(arr[:-1]) + ' and ' + arr[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaJoin(spam))
