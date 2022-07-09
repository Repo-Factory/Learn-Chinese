from pynput.keyboard import Listener
from threading import Thread
from threading import Event
from queue import Queue
from listener.helper import wrapper
from responder.responder import main


queue_event = Event()
text_queue = Queue()


translator_thread = Thread (
    target=main,
    args=(text_queue, queue_event)
    )
translator_thread.start()


listener = Listener(
       on_release=wrapper(text_queue, queue_event),
        )
listener.daemon = True
listener.start()


