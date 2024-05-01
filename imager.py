import pyautogui
import torch
import clip
import os
from PIL import Image
from pynput import keyboard

def crop_center(image, crop_width, crop_height):
    width, height = image.size
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = (width + crop_width) // 2
    bottom = (height + crop_height) // 2
    return image.crop((left, top, right, bottom))

print('MAKE SURE GOOGLE MAPS IS FULL SCREEN ON YOUR MONITOR AND THAT THE WINDOW RUNNING THIS SCRIPT IS VERY SMALL AND IN THE VERY CORNER OF THE SCREEN OR ON A SECOND MONITOR')

country = input("Input country you are generating data for: ")

data_path = 'data/archive/compressed_dataset/' + country + '/new' # change this according to where you put your data
count = 0

print('press n to take a screenshot')
def on_press(key):
    global count
    if key.char == 'n':
        print("\nScreenshotted!")
        image = pyautogui.screenshot()
        image = crop_center(image, 1536, 662)
        image.save(data_path + str(count) + '.jpg')
        
        count += 1
    else:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()