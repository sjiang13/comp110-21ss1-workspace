"""Which emoji set based on my friends are you?
Buzzfeed quiz - xp points are acquired by repeating the quiz, and bonus points are awarded when the player reads the directions.
For fun, the quiz questions are randomized to appear in different orders. 
The custom function points returns the xp values earned, and the function quiz_start calculates the sum of the ints associated with the quiz answered.
This sum is then put into the quiz_result function to return a sentence giving the players result."""

__author__ = "730411082"
from random import randint

quiz_total = 0 
player = ""
points = 0
NAMED_CONSTANT = "\U00000000"


def main() -> None:
  """Entrypoint of the program."""
  greeting = greet()
  is_playing: bool = True
  while is_playing: 
    print("1 Start Quiz \n2 Directions \n3 Quit Game")
    start_menu_choice = int(input("To continue, enter 1, 2, or 3: "))
    if start_menu_choice == 1:
      global quiz_total
      end_points = quiz_start(quiz_total)
      start_menu_choice = 3
      global points 
      points += 500
      print(quiz_result(end_points))
    if start_menu_choice == 2:
      instructions = directions()
    if start_menu_choice == 3:
      print("Thanks for playing, goodbye!")
      xp = xp_value(points)
      print(f"points =  {xp}")
    play_again: int = int(input("Play again? \n1 Yes \n2 No\nEnter the number of your choice: "))
    if play_again == 2:
      is_playing = False
  return None


def xp_value(xp: int) -> int:
  global points 
  return points


def directions() -> None:
  """Second menu option to read directions - will continue to ask for the correct input to continue."""
  global player
  print(f"Hello, {player}!")
  print("Directions:\nAfter each question is asked, use numbers 1, 2, 3, and 4 on your keyboard to select your answer.")
  next_input: int = int(input("Enter 1 to continue. "))
  while next_input != 1:
    next_input: int = int(input("Enter 1 to continue. "))
  print("1 Return to home\n2 Read directions again")
  return_menu: int = int(input("Enter the number of your choice: "))
  if return_menu == 1:
    print("Thanks for exploring!")
    global points
    points += 500
    print(f"points =  {points}")
    return None
  else: 
    directions()


def greet() -> None:
  """Greeting to user when quiz is started.""" 
  print("Welcome!")
  name: str = input("What is your name? ")
  global player
  player = name
  print(f"Hello, {player}! You are taking the quiz:\nWhich emoji set based on my friends are you?")
  return None


def quiz_start(total: int) -> int:
  """Quiz questions, where each answer is worth a different amount of points."""
  print("Which emoji set based on my friends are you?")
  question_order: int = randint(1,3)
  # print(question_order)
  if question_order == 1:
    # 1 = audrey 2 = kavya 3 = jamie 4 = me/jenny
    print("What is your ideal Saturday night?")
    print("1 Staying in \n2 Going to a party \n3 Movie night with friends \n4 Depends on how I feel")
    answer_1: int = int(input("Enter the number of your choice: "))

    print("Where do you most want to travel to?")
    print("1 Mexico \n2 Amsterdam \n3 Japan \n4 Italy")
    answer_2: int = int(input("Enter the number of your choice: "))

    print("Which is your favorite color?")
    print("1 Green \n2 Red \n3 Purple \n4 Blue")
    answer_3: int = int(input("Enter the number of your choice: "))

    print("Choose an ice cream flavor.")
    print("1 Mint Chocolate \n2 Coffee \n3 Raspberry \n4 Cookie Dough")
    answer_4: int = int(input("Enter the number of your choice: "))
    
  if question_order == 2:
    print("Choose an ice cream flavor.")
    print("1 Mint Chocolate \n2 Coffee \n3 Raspberry \n4 Cookie Dough")
    answer_1: int = int(input("Enter the number of your choice: "))

    print("Where do you most want to travel to?")
    print("1 Mexico \n2 Amsterdam \n3 Japan \n4 Italy")
    answer_2: int = int(input("Enter the number of your choice: "))

    print("What is your ideal Saturday night?")
    print("1 Staying in \n2 Going to a party \n3 Movie night with friends \n4 Depends on how I feel")
    answer_3: int = int(input("Enter the number of your choice: "))

    print("Which is your favorite color?")
    print("1 Green \n2 Red \n3 Purple \n4 Blue")
    answer_4: int = int(input("Enter the number of your choice: "))

  if question_order == 3:
    print("Which is your favorite color?")
    print("1 Green \n2 Red \n3 Purple \n4 Blue")
    answer_1: int = int(input("Enter the number of your choice: "))

    print("What is your ideal Saturday night?")
    print("1 Staying in \n2 Going to a party \n3 Movie night with friends \n4 Depends on how I feel")
    answer_2: int = int(input("Enter the number of your choice: "))

    print("Choose an ice cream flavor.")
    print("1 Mint Chocolate \n2 Coffee \n3 Raspberry \n4 Cookie Dough")
    answer_3: int = int(input("Enter the number of your choice: "))

    print("Where do you most want to travel to?")
    print("1 Mexico \n2 Amsterdam \n3 Japan \n4 Italy")
    answer_4: int = int(input("Enter the number of your choice: "))
  global quiz_total
  quiz_total = answer_1 + answer_2 + answer_3 + answer_4
  # print(points)
  return(quiz_total)


def quiz_result(total: int) -> str:
  """Quiz points converted into results."""
  # total min: 4 max 16 = 4, 5, 6, 7,   8, 9, 10       , 11, 12, 13, 14, 15, 16
  friend: str = ""
  emoji_result = ""
  global player
  name = player
  if total < 11:
    if total > 7:
      emoji_result = "\U00002615\U0001F41E\U0001F4DC\U0001F344"
      friend = "Kavya"
    else: 
      emoji_result = "\U0001F36F\U0001F33B\U0001F331\U0001F40C"
      friend = "Audrey"
  else:
    if total < 14:
      emoji_result = "\U0001F375\U0001F4DA\U0001F33A\U0001F349"
      friend = "Jamie"
    else:
      emoji_result = "\U0001F9E7\U0001F347\U0001F319\U0001F30F"
      friend = "Jenny"
  
  return(f"{name}, You are my friend {friend}, and your emoji set is {emoji_result}!")


if __name__ == "__main__":
  main()