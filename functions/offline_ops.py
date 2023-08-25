import os
import time

import pyautogui
from dotenv import load_dotenv

load_dotenv()

PATH_SCREENSHOT = os.getenv("PATH_SCREENSHOT")
screenshots = 1


def takeScreenShot():
    try:
        global screenshots
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(str(PATH_SCREENSHOT)+f"{screenshots}.jpg")
        screenshots += 1
    except Exception as e:
        print(e)
        return False

    return True


def typeAnything(string):
    time.sleep(1)
    pyautogui.write(string)
