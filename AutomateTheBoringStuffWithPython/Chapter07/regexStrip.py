""" Regex Version of strip()

Strips the given characters from the string.
If nothing is given, strips whitespace characters.
"""

def myStrip(string, regex = 'default'):
    import re

    # construct the regex
    if regex == 'default':
        regex = r'^\s*|\s*$'
    else:
        regex = r'^[{0}]*|[{0}]*$'.format(regex)

    # remove from the beginning and end
    return re.sub(regex, '', string)

myStr1 = "    haha hello my FRIEND !! \n \t"
myStr2 = "this is a great day for strip"

print(myStrip(myStr1), myStrip(myStr2, 'tphi'), sep = "\n")
