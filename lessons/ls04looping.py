"""Another looping example."""

some_int: int = int(input("Enter a number: "))

i: int = 1
total: int = 0
while i <= some_int:
    total += i
    i += 1


print(total)