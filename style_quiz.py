import time
import os
from body_matrix import body_matrix_quiz
from color_season import color_season_quiz
from style_roots import style_roots_quiz

# TO DO: on all quizzes we're assuming that the user is smart and will follow the instructions with inputs that make sense. The next iteration of this project will check to make sure that a permissible value is selected and return an error if one is not.
def style_quiz():
  print("Style Quiz based on the work of Body and Style by Ellie Jean Royden")
  quiz = input("Which quiz would you like to take? : press 1 for the Body Matrix Quiz, press 2 for the Color Season Quiz, press 3 for the Style Roots Quiz.")

  if quiz == ("1"):
    print("Loading Body Matrix Quiz...")
    time.sleep(5)
    os.system('clear')
    body_matrix_quiz()
  elif quiz == ("2"):
    print("Loading Color Season Quiz...")
    time.sleep(5)
    os.system('clear')
    color_season_quiz()
  else:
    print("Loading Style Roots Quiz...")
    time.sleep(5)
    os.system('clear')
    style_roots_quiz()

  again = input("Would you like to take another quiz? press 1 for Yes, press 2 for No.")

  if again == ("1"):
    style_quiz()
  else:
    print("Good bye! Thanks for taking the quiz!") 

style_quiz()