"""An exercise in computing the factorial of an int."""

__author__ = "730411082"


# Begin your solution here...
input_int: int = int(input("Choose a number: "))
factorial = 1
int_to_multiply = 1 
while int_to_multiply <= input_int: 
    factorial = factorial * int_to_multiply
    int_to_multiply += 1
    # print(factorial)
print(factorial)