"""A function to abbreviate strings."""

__author__ = "730411082"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Prompt the user for text....
    input_text: str = str(input("Write some text with some uppercase letters: "))
    abbreviation = abbreviate(input_text)
    print('The abbreviation is "' + abbreviation + '".')
    return None
    # .. and make use of abbreviate function and print it.


# TODO 1: Define the abbreviate function, and its logic, here.
def abbreviate(input_text: str) -> str:
    """Given an input string, returns the uppercase letters as an abbreviation."""
    abbreviation: str = ""
    i = 0
    while i < len(input_text):
        if input_text[i].isupper():
            abbreviation += str(input_text[i])
        i += 1
    return abbreviation


if __name__ == "__main__":
    main()