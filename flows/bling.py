import time
import pyautogui as auto
from pyautogui import ImageNotFoundException

auto.PAUSE = 0.5

from auto_functions import (
    click_on_img, copy_text_content,
    get_images_coordinates
)

phone_field_coordinates = None

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

        click_on_img("screenshots/bling_nome_aba.png")

        click_on_img("screenshots/bling_campo_codigo_rastreio.png")

        auto.typewrite(tracking_code)

        auto.press("enter")

        auto.hotkey("ctrl", "a")
        auto.press("backspace")

    def check_search_result():
        bad_search = True

        try:
            auto.locateOnScreen(
                "screenshots/bling_pesquisa_nenhum_resultado.png",
                confidence = 0.95
            )
        except ImageNotFoundException:
            bad_search = False

        try:
            auto.locateOnScreen(
                "screenshots/bling_remessa_cancelada.png",
                confidence = 0.95
            )
        except ImageNotFoundException:
            bad_search = False

        return bad_search

    search_customer_datas()

    bad_search = check_search_result()

    if not bad_search:

        result = get_images_coordinates(
            [
                ("screenshots/bling_email_field.png", 0.8),
                ("screenshots/bling_telefone_field.png", 0.8)
            ]
        )

        email_coordinates = result['bling_email_field']
        phone_field_coordinates = result['bling_telefone_field']

        print("[PROGRESS] Coletando email do usuário.\n")
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
        return True

    else: return False

def copy_customer_phone_number():
    """
    Copies the customer's phone number from the saved position.
    """
    print("[PROGRESS] Coletando número de telefone do usuário.\n")

    click_on_img("screenshots/bling_nome_aba.png")

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