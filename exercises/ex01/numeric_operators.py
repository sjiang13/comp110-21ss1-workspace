"""Numeric Operators Exercise!"""

__author__: str = "730411082"

# Your solution starts here...
left_side_str: str = input("What number is on the left hand side? ")
# print(type(left_side_str))
right_side_str: str = input("What number is on the right hand side? ")
left_int: int = int(left_side_str)
right_int: int = int(right_side_str)
# print(type(left_int))
# multiply = left_int**right_int
# print(multiply)
print(left_side_str + " ** " + right_side_str + ' is ' + str(left_int**right_int))
print(left_side_str + " / " + right_side_str + ' is ' + str(left_int/right_int))
print(left_side_str + " // " + right_side_str + ' is ' + str(left_int//right_int))
print(left_side_str + " % " + right_side_str + ' is ' + str(left_int%right_int))