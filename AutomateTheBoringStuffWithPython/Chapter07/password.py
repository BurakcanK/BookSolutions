""" Strong Password Detection

Determines if the given password is strong according to the rules;
- at least 8 character
- includes uppercase and lowercase
- at least one digit
"""

def isStrongPassword(password):
    import re
    # one regex for all the rules
    return bool(re.match(r"""^(?=.*[a-z])     # at least one lowercase (doesn't consume)
                              (?=.*[A-Z])     # at least one uppercase (doesn't consume)
                              (?=.*\d)        # at least one digit (doesn't consume)
                              [a-zA-Z0-9]{8,} # total 8 char long
                              $""", password, re.VERBOSE))

print(strongPassword('MyPrecious1'))
