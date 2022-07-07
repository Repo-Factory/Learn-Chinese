from pynput.keyboard import Listener
from listener.helper import outer
import threading
import multiprocessing
from learner.learner import parse_text

text_queue = multiprocessing.Queue()

if __name__ == "__main__":

    translator_thread = multiprocessing.Process (
        target=parse_text,
        args=(text_queue,)
        )
    translator_thread.start()



# Continual listening process
listener = Listener(
       on_release=outer(text_queue),
        )
listener.start()


