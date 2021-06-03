"""An exercise with functions and lists."""

__author__ = "730411082"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 3: Test your functions here
    # print(list_primes(2, 5))


# TODO 1: Define the is_prime function, and its logic, here.
def is_prime(number: int) -> bool:
    """Determine if a number is prime."""
    i: int = 2
    if number < i:
        return False
    while i < number:
        if number % i == 0:
            return False
        else:
            i += 1
    return True


# TODO 2: Define the list_primes function, and its logic, here.
def list_primes(num1: int, num2: int) -> list[int]:
    """In a range of numbers, create a list of primes."""
    result: list[int] = []
    for x in range(num1, num2):
        if is_prime(x) is True:
            result.append(x)
    return result       


if __name__ == "__main__":
    main()