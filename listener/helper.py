import pyautogui
import win32clipboard
from pynput.keyboard import Key
from time import sleep


# cleans the current terminal to see chinese more clearly"
new_page_string = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

# specific code sent to queue to exit
exit_code = 'bwerv73yn1n2398vnaoijenfvnfv891n23nhrnv93y4n75n5hvq89wehr7nvh49018hn7447hntv0918h3ntv9h1239ht8nv0193h8tn'


# pyautogui method that copies whatever is highlighted on screen
def copy_highlighted():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    sleep(.05) # sometimes the program will run faster than the autogui can copy


# gets information from the clipboard
def retrieve_clipboard():
    open_clipboard(100, .01)
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


# performs multiple attempts to open clipboard to avoid stagnating the program for a small clipboard error
def open_clipboard(retries, delay):
    while True:
        try:
            return win32clipboard.OpenClipboard()
        except Exception as e:
            if e.winerror!=5 or retries==0:
                raise
            retries = retries - 1
            sleep(delay)


# simple print method
def print_chinese(data):
    print(new_page_string)
    print(data)
    print('\n')


# calls functions for readability of on_release
def helper():
    copy_highlighted()
    data = retrieve_clipboard()
    print_chinese(data)
    return data


# puts data to queue when assigned key is pressed, and pushes exit code to queue on press of esc
def wrapper(queue, event):
    def on_release(key):
        if key == Key.esc:
            queue.put(exit_code)
            event.set()
        if key == Key.alt_l:
            data = helper()
            queue.put(data)
            event.set()
        return queue
    return on_release



