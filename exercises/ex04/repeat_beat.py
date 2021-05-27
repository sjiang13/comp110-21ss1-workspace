"""Repeating a beat in a loop."""

__author__ = "730411082"


# Begin your solution here...
input_beat: str = input("What beat do you want to repeat? ")

input_times: int = int(input("How many times do you want to repeat it? "))
input_spacing = " " + input_beat

final_str = ""
# print(final_str)
# print(len(final_str))
if input_times <= 0:
    final_str = final_str + "No beat..."
while input_times > 0:
    final_str = final_str + input_beat
    input_times -= 1
    input_beat = input_spacing

print(final_str)