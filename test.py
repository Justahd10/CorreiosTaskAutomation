import time
import pyautogui as auto

""" while True:
    time.sleep(1)
    print(auto.position()) """

""" time.sleep(2)
img_coordinates = auto.locateOnScreen("screenshots/bling_telefone_field.png", confidence = 0.8)

print(img_coordinates.left, img_coordinates.top)
auto.moveTo(img_coordinates.left, img_coordinates.top) """

print(auto.pixel(658, 759))