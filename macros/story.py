import pyautogui as pg
from time import sleep
from .image_paths import (skip_before_image, prepare_quest_image, start_image, skip_image, cancel_image, tap_image, next_quest_image)

pg.PAUSE = 0.5


def locate_and_click(image_path):
    try:
        image = pg.locateCenterOnScreen(image_path, confidence=0.8)
        if image is not None:
            pg.click(image)
            return True
    except pg.ImageNotFoundException:
        pass
    return False


def prepare_quest():
    while True:
        if locate_and_click(skip_before_image):
            sleep(3)
            pg.click()
            continue

        if locate_and_click(prepare_quest_image):
            break


def start_quest():
    while True:  
        sleep(2.5)
        if locate_and_click(start_image):
            break


def next_quest():
    while True:
        if locate_and_click(skip_image):
            continue

        if locate_and_click(cancel_image):
            continue

        if locate_and_click(tap_image):
            continue

        if locate_and_click(next_quest_image):
            break


def start_macro():
    while True:
        prepare_quest()
        start_quest()
        next_quest()
