import time
import os
import random

points = {"fire": 0, 
         "moon": 0, 
         "sun": 0,
         "flower": 0,
         "earth": 0,
         "mushroom": 0,
         "mountain": 0,
         "stone": 0}

words = {"fire":["sensual", "glamorous", "luxurious"], 
         "moon":["dark", "moody", "edgy"], 
         "sun":["playful", "experimental", "creative"], 
         "flower":["delicate", "airy", "intricate"], 
         "earth":["natural", "rugged", "outdoorsy"], 
         "mushroom":["simple", "neutral", "minimal"], 
         "mountain":["powerful", "formal", "professional"], 
         "stone":["sporty", "relaxed", "industrial"]}

url_order_list = [["fire", "moon", "sun"],
        ["flower", "moon", "sun"],
        ["flower", "fire", "sun"],
        ["earth", "fire", "sun"],
        ["earth", "fire", "moon"],
        ["earth", "flower", "fire"],
        ["earth", "moon", "sun"],
        ["earth", "flower", "moon"],
        ["earth", "flower", "sun"],
        ["stone", "moon", "sun"],
        ["stone", "fire", "sun"],
        ["stone", "fire", "moon"],
        ["stone", "flower", "sun"],
        ["stone", "flower", "moon"],
        ["stone", "flower", "fire"],
        ["stone", "earth", "sun"],
        ["stone", "earth", "moon"],
        ["stone", "earth", "fire"],
        ["stone", "earth", "flower"],
        ["mountain", "moon", "sun"],
        ["mountain", "flower", "sun"],
        ["mountain", "fire", "sun"],
        ["mountain", "flower", "moon"],
        ["mountain", "flower", "fire"],
        ["mountain", "earth", "fire"],
        ["mountain", "earth", "sun"],
        ["mountain", "earth", "moon"],
        ["mountain", "earth", "flower"],
        ["mountain", "stone", "sun"],
        ["mountain", "stone", "moon"],
        ["mountain", "stone", "fire"],
        ["mountain", "stone", "flower"],
        ["mushroom", "stone", "sun"],
        ["mushroom", "stone", "earth"],
        ["mushroom", "mountain", "fire"],
        ["mushroom", "mountain", "moon"],
        ["mushroom", "mountain", "sun"],
        ["mushroom", "stone", "fire"],
        ["mushroom", "mountain", "earth"],
        ["mushroom", "sun", "moon"],
        ["mushroom", "flower", "moon"],
        ["mushroom", "flower", "fire"],
        ["mushroom", "flower", "sun"],
        ["mushroom", "stone", "moon"],
        ["mushroom", "earth", "moon"],
        ["mushroom", "earth", "fire"],
        ["mushroom", "earth", "sun"],
        ["mushroom", "fire", "moon"],
        ["mushroom", "stone", "flower"],
        ["mushroom", "fire", "sun"],
        ["mountain", "stone", "earth"],
        ["mountain", "fire", "moon"],
        ["moon", "fire", "flower"]
        ]

def style_roots_quiz():

  print("Find which 3 Style Roots best describe YOUR style in 8 questions.")

  for i in range(8):
    # make a list of the keys, this will re-set for each question and will only be those with unused words
    key_choices = [key for key, value in words.items() if value != []]

    # choose 3 keys to get words from each of their values
    # remove it after it has been selected so no repeats in the same question
    key_1 = random.choice(key_choices)
    key_choices.remove(key_1)
    key_2 = random.choice(key_choices)
    key_choices.remove(key_2)
    key_3 = random.choice(key_choices)

    # choose a word from the list for each key
    word_1 = random.choice(words[key_1])
    word_2 = random.choice(words[key_2])
    word_3 = random.choice(words[key_3])

    # ask user to pick one of the words
    answer = input(f"{i+1}. Choose a Word from the following: press 1 for {word_1}, press 2 for {word_2}, press 3 for {word_3}.")

    # record the points using the keys and remove the word that was selected so it can't be used again.
    if answer == ("1"):
      points[key_1] += 1
      words[key_1].remove(word_1)
    elif answer == ("2"):
      points[key_2] += 1
      words[key_2].remove(word_2)
    else:
      points[key_3] += 1 
      words[key_3].remove(word_3) 

    time.sleep(2)
    os.system('clear')  


  # Sort the dictionary by values in descending order
  sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)

  # Get the first, second, and third largest values (some points may be tied, that is okay)
  style_roots_list = [sorted_points[0][0], sorted_points[1][0], sorted_points[2][0]]

  # check the urls_list for the one matching the list above
  for list in url_order_list:
    if sorted(list) == sorted(style_roots_list):
    # put it in the correct format
      url_ending = list[0] + "-x-" + list[1] + "-x-" + list[2] + "/"

  # the whole url
  pinterest_url = f"https://uk.pinterest.com/elliejeanroyden/style-roots-combinations/{url_ending}"

  # show user their results
  print("Calculating your results...")
  time.sleep(5)
  os.system('clear')
  print(f"Your style roots are: {sorted_points[0][0]}, {sorted_points[1][0]}, and {sorted_points[2][0]}!") 
  print(f"Go to this link for some style inspiration: {pinterest_url}")
  time.sleep(5)

