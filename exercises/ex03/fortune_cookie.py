"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730411082"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


random_int: int = randint(1, 4)
# print(random_int)
if random_int < 3:
    if random_int != 1:
        fortune = "You will have a fantastic day!"
    else: 
        fortune = "Expect financial success soon!"
else:
    if random_int > 3:
        fortune = "Good news is in your future."
    else: 
        fortune = "Someone important will appear in your life."



print("Your fortune cookie says..")
print(fortune)
print("Now, go spread positive vibes!")