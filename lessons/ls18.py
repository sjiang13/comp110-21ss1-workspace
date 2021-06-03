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