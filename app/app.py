'''
app.py is the starting point for the program where the threads are initiated
There is a listener thread and a main thread which responds
to the information taken in by the listener and its helper methods.
The listener will place information into the queue when the assigned key is pressed
When this event occurs, the main thread will the translator methods to return translated chinese

'''

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


