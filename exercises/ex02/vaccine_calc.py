"""A vaccination calculator."""

__author__ = "730411082"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop_input: str = input("Population: ")
administered_doses_input: str = input("Doses administered: ")
dose_per_day: str = input("Doses per day: ")
target_per: str = input("Target percent vaccinated: ")
pop_int: int = int(pop_input)
administered_doses_int: int = int(administered_doses_input)
dose_per_day_int: int = int(dose_per_day)
target_per_int: int = int(target_per)
today: datetime = datetime.today()
# print(today)
vaccines_needed: int = (2 * pop_int) 
# print("vaccines needed = " + str(vaccines_needed))

total_needed: float = (vaccines_needed * target_per_int / 100)
# print("total vaccines needed to reach target = " + str(target_vaccines_needed))
target_vaccines_needed: int = round(total_needed)
remaining_doses_needed: float = (target_vaccines_needed - administered_doses_int)
# print("doses remaining to reach target = " + str(remaining_doses_needed))

# remaining_doses_needed_round: int = round(remaining_doses_needed)
# print("rounded:" + str(remaining_doses_needed_round))
days_needed: float = remaining_doses_needed / dose_per_day_int
print(days_needed)

days_needed_rounded: int = round(days_needed)
days_needed_str: str = str(days_needed_rounded)
# print(days_needed)
goal_date: datetime = today + timedelta(days_needed)
print("We will reach " + target_per + "% vaccination in " + 
    days_needed_str + " days, which falls on " + (goal_date.strftime("%B %d, %Y")))