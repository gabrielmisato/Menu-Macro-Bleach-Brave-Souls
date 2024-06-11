import pyautogui as pg
from time import sleep
from .image_paths import (start_image, pause_image, tap_image, close_image, cancel_image, retry_image, retry_net_image, ok_image, menu_image, gift_box_image, soul_ticket_page_image, collect_all_image, empty_box_image)

pg.PAUSE = 0.5


def locate_and_click(image_path):
    try:
        if image_path != pause_image:  
            image = pg.locateCenterOnScreen(image_path, confidence=0.8)
            if image is not None:
                pg.click(image)
                return True
        else:
            image = pg.locateCenterOnScreen(image_path, confidence=0.8)
            if image is not None:
                return True
    except pg.ImageNotFoundException:
        pass
    return False


def start_quest():
    while True:
        if locate_and_click(retry_net_image):
            continue

        if locate_and_click(cancel_image):
            open_gift_box()

        if locate_and_click(start_image):
            continue
        
        if locate_and_click(pause_image):
            break


def open_gift_box():
    while True:          
        if locate_and_click(menu_image):
            gitf_box = pg.locateOnScreen(gift_box_image, confidence=0.7)
            pg.click(gitf_box)
            sleep(3)

            soul_ticket = pg.locateOnScreen(soul_ticket_page_image, confidence=0.8)
            pg.click(soul_ticket)

            empty_box = pg.locateOnScreen(empty_box_image, confidence=0.8)
            if empty_box is not None:
                close = pg.locateOnScreen(close_image, confidence=0.8)
                pg.click(close)
                raise SystemExit
            else:
                claim = pg.locateOnScreen(collect_all_image, confidence=0.8)
                pg.click(claim)

                ok = pg.locateOnScreen(ok_image, confidence=0.8)
                pg.click(ok)
                sleep(3)

                close = pg.locateOnScreen(close_image, confidence=0.8)
                pg.click(close)
                sleep(0.5)
                pg.click()
                start_quest()
                break


def tap_screen():
    while True:
        if locate_and_click(close_image):
            continue

        if locate_and_click(cancel_image):
            continue

        if locate_and_click(retry_image):
            continue

        if locate_and_click(tap_image):
            sleep(1)
            pg.click()
            sleep(0.5)
            pg.click()
            break
    

def retry():
    while True:
        if locate_and_click(close_image):
            continue

        if locate_and_click(retry_image):
            continue

        if locate_and_click(retry_image):
            continue

        if locate_and_click(start_image):
            break


def start_macro():
    while True:
        start_quest()
        tap_screen()
        retry()
