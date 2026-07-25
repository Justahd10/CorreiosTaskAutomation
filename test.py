import time
import pyautogui as auto
from pyautogui import ImageNotFoundException

while True:
    time.sleep(1)
    print(auto.position())

""" time.sleep(2)
img_coordinates = auto.locateOnScreen("screenshots/bling_telefone_field.png", confidence = 0.8)

print(img_coordinates.left, img_coordinates.top)
auto.moveTo(img_coordinates.left, img_coordinates.top) """
""" 
while True:
    try:
        coordinates =\
            auto.center(
                auto.locateOnScreen(
                    "screenshots/omni_botao_abrir_conversa.png",
                    confidence = 0.95
                )
            )
    except ImageNotFoundException:
        print("Imagem não encontrada")
    else:
        auto.moveTo(coordinates)
        print("Encontrado!")
        break
    finally:
        time.sleep(0.25) """