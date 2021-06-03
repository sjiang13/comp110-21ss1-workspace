"""A simple function to sum up a list."""


def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned."""
    total: int = 0
    i: int = 0
    # while i < len(xs):
    #     total += xs[i]
    #     i += 1 

    for e in xs:
        total += e
    return total

def sum_two_lists(xs: list[int], ys: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(0, len(xs)):
        result.append(xs[1] + ys[i])
    return result
    # i: int = 0
    # while i < len(xs):
    #   result.append(xs[i] + ys[i])
    #   i += 1
