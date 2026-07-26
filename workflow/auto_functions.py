import time
import pyautogui as auto
from pyautogui import ImageNotFoundException


auto.PAUSE = 0.5


def click_on_img(img_file, confidence = 0.7):
    """
    Locates an image on the screen and clicks its center.

    Args:
        img_file: Path to the image file to be located.
        confidence: Confidence level for image matching.
        delay: Cursor movement time to the element.
    """
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

    # If found, click on image directly at the detected coordinates
    if result['found_image']:
        auto.click(
            result['coordinates'].x,
            result['coordinates'].y
        )


def click_on_imgs_sequence(images_files: list[tuple], interval = 1):
    """
    Click on a sequence of images with a specified interval
    """
    for item in images_files:
        click_on_img(item[0], item[1])
        time.sleep(interval)


def copy_text_content(
    start_positions: list[tuple[int]],
    drag_positions: list[tuple[int]], 
    end_positions: list[tuple[int]],
    delay = 1
):
    """
    Selects text on the screen and copies it to the 
    clipboard.

    Args:
        start_positions: Initial cursor positions to begin 
        the selection. drag_positions: Intermediate drag 
        positions for the selection. end_positions: Final 
        positions to finish the selection. delay: Cursor 
        movement time between positions.
    """
    def move_over_positions(positions_list):
        nonlocal delay
        for position in positions_list:
            auto.moveTo(position, duration = delay)

    # Prepare the mouse for start to copy text content
    move_over_positions(start_positions)

    auto.mouseDown(button = "left")

    # Select text content to copy
    move_over_positions(drag_positions)

    auto.hotkey("ctrl", "c")

    # Finally preapre for mouse up
    move_over_positions(end_positions)

    auto.mouseUp(button = "left")


def get_images_coordinates(files: list[tuple]):
    """Returns the coordinates of a list of images found on the screen."""
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


def run_keys_sequence(keybowards: list):
    """
    Presses a sequence of keys with a small interval between 
    them.
    """
    for key in keybowards:
        auto.press(key)
        time.sleep(0.1)