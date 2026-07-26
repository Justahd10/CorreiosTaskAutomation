import pyautogui as auto, keyboard, pathlib
from pyautogui import ImageNotFoundException

from workflow.auto_functions import (
    click_on_img, copy_text_content,
    get_images_coordinates, click_on_imgs_sequence
)

auto.PAUSE = 1
phone_field_coordinates = None

# Access relative path  fot images folder
imgs_path = (pathlib.Path.cwd() / "screenshots").as_posix()



def copy_customer_email(tracking_code):
    """Searches for the customer in Bling and copies the contact data.

    Args:
        tracking_code: Tracking code used in the customer search.

    Returns:
        True when the search finds valid data; False when there is no result
        or the shipment is canceled.
    """
    global phone_field_coordinates

    def search_customer_datas():
        nonlocal tracking_code

        click_on_imgs_sequence(
            [
                (imgs_path + "/bling_nome_aba.png", 0.99),
                (imgs_path + "/bling_campo_codigo_rastreio.png", 0.99)
            ],
            interval = 0
        )

        keyboard.write(tracking_code)

        auto.press("enter")

        auto.hotkey("ctrl", "a")
        auto.press("backspace")

    def check_search_result():
        fail_search = False

        try:
            auto.locateOnScreen(
                imgs_path + "/bling_pesquisa_nenhum_resultado.png",
                confidence = 0.95
            )
        except ImageNotFoundException:
            pass
        else:
            print("Nenhum resultado de pesquisa no bling.")
            fail_search = True

        try:
            auto.locateOnScreen(
                imgs_path + "/bling_remessa_cancelada.png",
                confidence = 0.95
            )
        except ImageNotFoundException:
            pass
        else:
            print("Status cancelado na pesquisa no bling.")
            fail_search = True

        return fail_search

    search_customer_datas()

    fail_search = check_search_result()

    if not fail_search:

        result = get_images_coordinates(
            [
                (imgs_path + "/bling_email_field.png", 0.8),
                (imgs_path + "/bling_telefone_field.png", 0.85)
            ]
        )
        
        email_coordinates = result[
            imgs_path + "/bling_email_field.png"
        ]
        phone_field_coordinates = result[
            imgs_path + "/bling_telefone_field.png"
        ]

        print("[PROGRESS] Coletando email do usuário.\n\n")
        copy_text_content(
            delay = 0.25,
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

        auto.click() # <- reset the current selection on the page

        return True

    else: return False

def copy_customer_phone_number():
    """
    Copies the customer's phone number from the saved position.
    """
    print("[PROGRESS] Coletando número de telefone do usuário.\n")

    click_on_img(imgs_path + "/bling_nome_aba.png")

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