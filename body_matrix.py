import time
import os

answer_key = {
  "width":{"1":"wide", "2":"medium", "3":"narrow"}, 
  "vertical":{"1":"long", "2":"medium", "3":"short"}, 
  "shape":{"1":"round", "2":"medium", "3":"narrow"}
  }

def body_matrix_quiz():
  print("Welcome to the Body Matrix Quiz (3 Questions)")
  time.sleep(2)
  os.system('clear')
  print("When answering these questions, think about your answers related to your own proportions and your experiences when trying on clothes. Do not compare your beautiful self to others.")
  time.sleep(5)
  os.system('clear')
  width = answer_key["width"][input("1. In relation to your own proportions, are your shoulders: press 1 for wide, press 2 for medium, press 3 for narrow")]
  time.sleep(2)
  os.system('clear')
  vertical = answer_key["vertical"][input("2. People usually guess my height as ______ I actually am. press 1 for taller than, press 2 for the same as, press 3 for shorter than")]
  time.sleep(2)
  os.system('clear')
  shape = answer_key["shape"][input("3. I have to think about curve (upper body, lower body, or both) when selecting clothing and I look best in outfits that emphasize my waist. press 1 for Always, press 2 for Sometimes, press 3 for Never")]
  time.sleep(2)
  os.system('clear')


  url_ending = width + "-+-" + vertical + "-+-" + shape + "/"
  pinterest_url = f"https://uk.pinterest.com/elliejeanroyden/the-body-matrix/{url_ending}"
  print("Calculating your results...")
  time.sleep(5)
  os.system('clear')
  print(f"Your body matrix type is: {width}, {vertical}, {shape}!") 
  print(f"Go to this link for some style inspiration: {pinterest_url}")
  time.sleep(5)
  
