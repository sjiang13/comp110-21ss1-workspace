"""Examples of dictionaries."""


# Establish a type with the following syntax:
# dict[keytype, value type]
# empty dictionary literal is {}

players: dict[str, int] = {}

# insert a new key-value pair
players["Brooks"] = 15
# Reference keys inside subscription notatiuon, associated
# values are assigned on RHS of assignment operator
players["Love"] = 2
players["Bacot"] = 4
players["Bacot"] = players["Bacot"] + 1
print(players)

def passes(students:dict[str, float]) -> list[str]:
    """Given student info, who passes?"""
    result: list[str] = []
    for student in students:
        if students[student] > 60:
            result.append(student)

    return result

s: dict[str, float] = {"Andrew": 100.0, "Shaurik": 89.0, "Claire": 40.0}
print(passes(s))

teachers_pet: list[str] = ["Claire", "Jasper"]

for pet in teachers_pet:
    # initialize or increment
    if pet in s:
        # increment since the pet key is valid, and exists in the s dictionary
        s[pet] += 50.0
    else:
        # initializing bc the key is not yet in the dictionary
        s[pet] = 65.0

frequency_table: dict[str, int] = {}
# for each color in input dictionry
# if the color is already in teh table, increment its value
# if not, add it to the table with a starting value of 1

print(s)

a: list[int] = [1, 2, 3, 4, 5, 6]
b: list[int] = [2, 4, 6]

for e in a: 
    if e not in b:
        print(f"NO {e} is not in list b!")


def max_algo(xs: list[int]) -> int:
    # make the assumption that the list is not empty
    result: int = xs[0]
    for item in xs:
        if item > result:
            result = item
    return result

# steps for finding favorite color:
# 1. make frequency table, looping over the input parameter (keys or values)
# initialize vs increment pattern
# 2. max color - perform the max algorithm
# keep track of not only the curent max as we go, but also the color associated with the max