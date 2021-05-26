"""An exercise in remainders and boolean logic."""

__author__ = "730411082"


# Begin your solution here...
given_int: int = int(input("Enter an int: "))
if given_int % 2 == 0 and given_int % 7 == 0:
    print("TAR HEELS")
else:
    if given_int % 2 == 0:
        print("TAR")
    if given_int % 7 == 0:
        print("HEELS")
    if given_int % 2 != 0 and given_int % 7 != 0:
        print("CAROLINA")