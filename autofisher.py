from PIL import ImageGrab
import keyboard
import pyautogui
import time


def check_for_bite():
    image = ImageGrab.grab(bbox=(940, 380, 1000, 440))
    for x in range(60):
        for y in range(60):
            if image.getpixel((x, y)) == (255, 255, 255):
                print("fish bit")
                return True


def pull_fish():
    image = ImageGrab.grab(bbox=(755, 835, 1165, 870))
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x, y)) == (197, 42, 0):
                return False
            if image.getpixel((x, y)) == (71, 222, 13):
                return 'caught'
    return True


stop = False

keyboard.wait("p")

while not stop:
    pyautogui.mouseDown(button='right')
    time.sleep(.15)
    pyautogui.mouseUp(button='right')
    while not check_for_bite():
        if keyboard.is_pressed('q'):
            exit()
        check_for_bite()
    time.sleep(1)
    pyautogui.click(button='right')

    while pull_fish() != 'caught':
        if keyboard.is_pressed('q'):
            exit()
        if pull_fish():
            print('reeling')
            pyautogui.mouseDown(button='right')
        else:
            print('releasing')
            pyautogui.mouseUp(button='right')