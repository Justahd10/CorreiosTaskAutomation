import time
import pyautogui as auto
from pyautogui import ImageNotFoundException


def click_on_img(img_file, confidence = 0.7, delay = 0):
    # Try locate screenshot on browser window
    def get_screenshoot_coordinates():
        nonlocal img_file, confidence

        result = {
            "found_image": True,
            "coordinates": None
        }

        try:
            result['coordinates'] = auto.center(
                auto.locateOnScreen(
                    img_file, confidence = confidence
                )
            )
        except ImageNotFoundException:
            result['found_image'] = False
            print(f"Screenshot from {img_file} not found")

            return result

        return result

    result = get_screenshoot_coordinates()

    # If found, click on image
    if result['found_image']:
        auto.moveTo(
            result['coordinates'],
            duration = delay
        )
        time.sleep(0.5)
        auto.click()


def copy_text_content(
    start_positions: list[tuple[int]],
    drag_positions: list[tuple[int]], 
    end_positions: list[tuple[int]],
    delay = 1
):
    def move_over_positions(positions_list):
        nonlocal delay
        for position in positions_list:
            auto.moveTo(position, duration = delay)
            time.sleep(0.5)

    # Prepare the mouse for start to copy text content
    move_over_positions(start_positions)

    auto.mouseDown(button = "left")
    time.sleep(0.5)

    # Select text content to copy
    move_over_positions(drag_positions)

    auto.hotkey("ctrl", "c")
    time.sleep(0.5)

    # Finally preapre for mouse up
    move_over_positions(end_positions)

    auto.mouseUp(button = "left")
    time.sleep(0.5)


def get_images_coordinates(files: list[tuple]):
    coordinates = {}

    for file in files:
        try:
            coordinate = auto.locateOnScreen(
                image = file[0], confidence = file[1]
            )
            coordinates[
                (
                    file[0].replace("screenshots/", "")
                ).replace(".png", "")
            ] = {
                "x": int(coordinate.left),
                "y": int(coordinate.top)
            }
        except ImageNotFoundException:
            coordinates[
                (
                    file[0].replace("screenshots/", "")
                ).replace(".png", "")
            ] = {
                "x": None, "y": None
            }

    return coordinates


def put_trigger(trigger_type, values):

    def put_rgb_change_trigger():
        nonlocal values
        trigger_value =\
            auto.pixel(values[0], values[1])

        print("Procurando por mudança RGB...")

        while auto.pixel(
            values[0], values[1]
        ) == trigger_value:
            trigger_value = auto.pixel(
                values[0], values[1]
            )
            time.sleep(0.25)

        print("Mudança de RGB encontrada!")

    # Trigger execution handling
    match trigger_type:
        case "rgb_change":
            put_rgb_change_trigger()


def run_keys_sequence(keybowards: list):
    for key in keybowards:
        auto.press(key)
        time.sleep(0.25)