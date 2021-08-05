import pyautogui
import random
import re

# Get screen size
screen_size = re.split("=|,|\)", str(pyautogui.size()))

# Start moving mouse
try:
    while True:
        pyautogui.moveTo(random.randint(0, int(screen_size[1])), random.randint(0, int(screen_size[3])), duration=1)

# Break out of loop on key click
except KeyboardInterrupt:
    pass
