# puts data to queue when assigned key is pressed, and pushes exit code to queue on press of esc
from pynput.keyboard import Key
from app.listener.helper import exit_code
from app.listener.helper import helper


def on_release_wrapper(queue, event):
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
