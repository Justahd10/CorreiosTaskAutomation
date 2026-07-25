import time
import pyautogui as auto
from auto_functions import (
    click_on_img, copy_text_content,
    get_images_coordinates, put_trigger
)

phone_field_coordinates = None

def copy_customer_email(tracking_code):
    global phone_field_coordinates

    print(f"Iniciando processo para o código de rastreio {tracking_code}.")

    # 1. Access invoices manager web page
    click_on_img("screenshots/bling_nome_aba.png")
    time.sleep(0.5)

    # 2. Access trakcing code filtering fild
    click_on_img("screenshots/bling_campo_codigo_rastreio.png")

    # 3. Type Correios tracking code
    auto.typewrite(tracking_code)

    # 4. Search by tracking code
    auto.press("enter")
    time.sleep(0.25)

    # 5. Wait load
    time.sleep(3)

    auto.hotkey("ctrl", "a")
    time.sleep(0.25)
    auto.press("backspace")



    # 6. Copy User email addres
    result = get_images_coordinates(
        [
            ("screenshots/bling_email_field.png", 0.8),
            ("screenshots/bling_telefone_field.png", 0.8)
        ]
    )
    print(result)
    email_coordinates = result['bling_email_field']
    phone_field_coordinates = result['bling_telefone_field']

    copy_text_content(
        delay = 0.5,
        start_positions = [
            (
                email_coordinates['x'],
                email_coordinates['y']
            ),
            (
                email_coordinates['x'],
                email_coordinates['y'] + 50
            )
        ],
        drag_positions = [
            (
                phone_field_coordinates['x'] - 20,
                email_coordinates['y'] + 50
            )
        ],
        end_positions = [
            (
                phone_field_coordinates['x'] - 20,
                email_coordinates['y'] + 90
            )
        ]
    )

def copy_customer_phone_number():
    print("Copiando o número de telefone...")
    # 1. Access invoices manager web page
    click_on_img("screenshots/bling_nome_aba.png")
    time.sleep(0.5)

    # 2. Copy User phone number
    copy_text_content(
        delay = 0.25,
        start_positions = [
            (
                phone_field_coordinates['x'],
                phone_field_coordinates['y']
            ),
            (
                phone_field_coordinates['x'],
                phone_field_coordinates['y'] + 50
            )
        ],
        drag_positions = [
            (
                phone_field_coordinates['x'] + 140,
                phone_field_coordinates['y'] + 50
            )
        ],
        end_positions = [
            (
                phone_field_coordinates['x'] + 20,
                phone_field_coordinates['y'] + 90
            )
        ]
    )

    print("Número de telefone copiado!")