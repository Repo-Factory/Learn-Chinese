import pyautogui
import win32clipboard
from pynput.keyboard import Key
import time


def copy_highlighted():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')


def retrieve_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def wrapper(queue, event):
    def on_release(key):
        if key == Key.esc:
            exit()
        if key == Key.alt_l:
            copy_highlighted()
            data = retrieve_clipboard()
            print(data)
            queue.put(data)
            event.set()
        return queue
    return on_release

