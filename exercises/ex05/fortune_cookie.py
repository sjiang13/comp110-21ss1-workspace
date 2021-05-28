"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730411082"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
random_int = randint(1, 4)


def fortune_cookie() -> str:
    """Returns fortune."""
    fortune: str = ""
    if random_int < 3:
        if random_int != 1:
            fortune = "You will have a fantastic day!"
        else: 
            fortune = "Expect financial success soon!"
    elif random_int > 3:
        fortune = "Good news is in your future."
    else: 
        fortune = "Someone important will appear in your life."
    return fortune


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()