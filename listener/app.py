from pynput.keyboard import Listener
from listener.helper import wrapper
import threading
from translator.translator import parse_text
from queue import Queue
from threading import Lock
from threading import Event

event = Event()
text_queue = Queue()
#put_lock = Lock()
#get_lock = Lock()

translator_thread = threading.Thread (
    target=parse_text,
    args=(text_queue, event)
    )
translator_thread.start()


# Continual listening process

listener = Listener(
       on_release=wrapper(text_queue, event),
        )
listener.start()


