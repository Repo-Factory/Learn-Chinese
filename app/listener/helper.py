import pyautogui
import pyperclip
from time import sleep


# cleans the current terminal to see chinese more clearly"
new_page_string = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTranslation starting... thread can't be stopped "\
                  "until translation is finished. Do not press alt again until complete"\
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


# resets page
close_page_string = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'


# specific code sent to queue to exit
exit_code = 'bwerv73yn1n2398vnaoijenfvnfv891n23nhrnv93y4n75n5hvq89wehr7nvh49018hn7447hntv0918h3ntv9h1239ht8nv0193h8tn'


# pyautogui method that copies whatever is highlighted on screen
def copy_highlighted():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    sleep(.05) # sometimes the program will run faster than the autogui can copy


# simple print method
def print_chinese(data):
    print(new_page_string)
    print(data)
    print('\n')


# calls functions for readability in listener
def helper():
    copy_highlighted()
    data = pyperclip.paste()
    print_chinese(data)
    return data


# print helpers
def print_full_trans():
    print('\n')


def print_complete():
    print('\n\n\n translation complete....')




