import pyautogui
import win32clipboard
from pynput.keyboard import Key
from time import sleep


def copy_highlighted():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    sleep(.05)


def retrieve_clipboard():
    open_clipboard(100, .01)
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def open_clipboard(retries, delay):
    while True:
        try:
            return win32clipboard.OpenClipboard()
        except Exception as e:
            if e.winerror!=5 or retries==0:
                raise
            retries = retries - 1
            sleep(delay)


def wrapper(queue, event):
    def on_release(key):
        if key == Key.esc:
            queue.put('exit code: FC789456')
            event.set()
        if key == Key.alt_l:
            copy_highlighted()
            data = retrieve_clipboard()
            print(data)
            queue.put(data)
            event.set()
        return queue
    return on_release
