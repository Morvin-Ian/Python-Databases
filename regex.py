import re

# \d- Any numeric digit from 0 to 9.
# \D- Any character that is not a numeric digit from 0 to 9.
# \w- Any letter, numeric digit, or the underscore character.
# (Think of this as matching “word” characters.)
# \W- Any character that is not a letter, numeric digit, or the
# underscore character.
# \s- Any space, tab, or newline character. (Think of this as
# matching “space” characters.)
# \S- Any character that is not a space, tab, or newline


# (*) Asterik is used to match zero or more
# Mor(vi)*n means the match can be Morn, Morvivin, Morvivivin...

# (+) Plus is used to match one or more
# Mor(vi)+n means the match can be Morvin, Morvivin, Morvivivin...

# {} Braces are Used to monitor repetitions
#  Mor(vi){3}n matches Morvivivin
# Mor(vi){3,5}n matches Morvivivin- (Nongreedy matching), Morvivivivin, or Morvivivivivin-(Greedy matching)

# ^ -Match the start of a string
# $ -Match the end of a string

# # Use of parathesis
# phone_number = re.compile(r'(\d\d\d)(\d\d\d\d\d\d\d\d\d')
# match = phone_number.search(input())
# match.group(1) = country code
# match.group(2) = the second pair

# ? -It is used to indicate an oprion
# E.g the number below is a match even if the first are missing. 




email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
match = email.search(input('Email: '))

# The search method yields the first match
# The findall method yields a string of all matches

if (match):
    print(f"Valid: {match.group()}")
else:
    print("Invalid Email")


