import time
import os


scoring = {
    ('warm', 'dark', 'soft'):"true-autumn", 
    ('warm', 'dark', 'bright'):"dark-autumn",
    ('warm', 'light', 'soft'):"true-spring",
    ('warm', 'light', 'bright'):"true-spring",
    ('warm', 'soft', 'dark'):"true-autumn",
    ('warm', 'bright', 'dark'):"bright-spring",
    ('warm', 'soft', 'light'):"true-spring",
    ('warm', 'bright', 'light'):"true-spring",
    ('cool', 'dark', 'soft'):"dark-winter",
    ('cool', 'dark', 'bright'):"true-winter",
    ('cool', 'light', 'soft'):"true-summer",
    ('cool', 'light', 'bright'):"light-summer",
    ('cool', 'soft', 'dark'):"soft-summer",
    ('cool', 'bright', 'dark'):"true-winter",
    ('cool', 'soft', 'light'):"true-summer",
    ('cool', 'bright', 'light'):"bright-winter",
    ('dark', 'warm', 'soft'):"true-autumn",
    ('dark', 'warm', 'bright'):"dark-autumn",
    ('dark', 'cool', 'soft'):"dark-winter",
    ('dark', 'cool', 'bright'):"true-winter",
    ('dark', 'soft', 'warm'):"true-autumn",
    ('dark', 'soft', 'cool'):"dark-winter",
    ('dark', 'bright', 'warm'):"dark-autumn",
    ('dark', 'bright', 'cool'):"true-winter",
    ('light', 'warm', 'soft'):"light-spring",
    ('light', 'warm', 'bright'):"light-spring",
    ('light', 'cool', 'soft'):"true-summer",
    ('light', 'cool', 'bright'):"light-summer",
    ('light', 'soft', 'warm'):"light-spring",
    ('light', 'soft', 'cool'):"true-summer",
    ('light', 'bright', 'warm'):"light-spring",
    ('light', 'bright', 'cool'):"light-summer",
    ('soft', 'warm', 'dark'):"true-autumn",
    ('soft', 'warm', 'light'):"soft-autumn",
    ('soft', 'cool', 'dark'):"soft-summer",
    ('soft', 'cool', 'light'):"true-summer",
    ('soft', 'dark', 'warm'):"true-autumn",
    ('soft', 'dark', 'cool'):"soft-summer",
    ('soft', 'light', 'warm'):"soft-autumn", 
    ('soft', 'light', 'cool'):"true-summer",
    ('bright', 'warm', 'dark'):"bright-spring",
    ('bright', 'warm', 'light'):"bright-spring",
    ('bright', 'cool', 'dark'):"true-winter",
    ('bright', 'cool', 'light'):"bright-winter",
    ('bright', 'dark', 'warm'):"bright-spring",
    ('bright', 'dark', 'cool'):"true-winter",
    ('bright', 'light', 'warm'):"bright-spring", 
    ('bright', 'light', 'cool'):"bright-winter"
  }


def color_season_quiz():

  answer_key = {
  "tone":[{"1":"warm", "2":"cool"}, "warm vs. cool"], 
  "depth":[{"1":"dark", "2":"light"}, "dark vs. light"],
  "clarity":[{"1":"soft", "2":"bright"}, "soft vs. bright"]
  }

  print("Welcome to the Color Season Quiz (6 Questions)")
  time.sleep(2)
  os.system('clear')
  tone = answer_key["tone"][0][input("1. When thinking about color in all of your features (hair, skin, and eyes) are they more: press 1 for warm-toned, press 2 for cool-toned")]
  answer_key['tone'].insert(2, tone)
  time.sleep(2)
  os.system('clear')
  depth = answer_key["depth"][0][input("2. The colors in my features are a ____ shade of that color. press 1 for dark, press 2 for light")]
  answer_key['depth'].insert(2, depth)
  time.sleep(2)
  os.system('clear')
  clarity = answer_key["clarity"][0][input("3. The colors in my features are a ____ shade of that color. press 1 for soft and muted, press 2 for bright and clear")]
  answer_key['clarity'].insert(2, clarity)
  time.sleep(2)
  os.system('clear')

  ranked_answers = []

  for value in answer_key.values():
    number = input(f"Rank your traits from 1-3, 1 being the easiest question for you to answer, 3 being the most difficult. Use each number only once. {value[1]}")
    ranked_answers.insert(int(number)-1, value[2])
    time.sleep(2)
    os.system('clear')

  results = scoring[tuple(ranked_answers)]

  url_ending =  results + "-style/"
  pinterest_url = f"https://uk.pinterest.com/elliejeanroyden/colour-seasons/{url_ending}"
  print("Calculating your results...")
  time.sleep(5)
  os.system('clear')
  print(f"Your color season is: {str(results).replace('-', ' ')}!") 
  print(f"Go to this link for some style inspiration: {pinterest_url}")
  time.sleep(5)


