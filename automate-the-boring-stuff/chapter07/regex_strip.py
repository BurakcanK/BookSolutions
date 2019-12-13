"""Regex Version of strip()

Strip the given characters from the string.
If nothing is given, strip whitespace characters.
"""


def my_strip(s, regex="default"):
    import re

    # construct the regex
    if regex == "default":
        regex = r"^\s*|\s*$"
    else:
        regex = r"^[{0}]*|[{0}]*$".format(regex)

    # remove from the beginning and end
    return re.sub(regex, "", s)


str1 = "    haha hello my FRIEND !! \n \t"
str2 = "this is a great day for strip"

print(my_strip(str1), my_strip(str2, "tphi"), sep="\n")
