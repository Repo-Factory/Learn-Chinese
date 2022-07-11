'''
main.py is the starting point for the program where the threads are initiated
There is a listener thread and a main thread which responds
to the information taken in by the listener and its helper methods.
The listener will place information into the queue when the assigned key is pressed
When this event occurs, the main thread will call the translator methods to return translated chinese
'''

from pynput.keyboard import Listener
from threading import Thread
from threading import Event
from queue import Queue
from app.listener.listener import on_release_wrapper
from app.responder.responder import respond


def main():
    queue_event = Event()
    text_queue = Queue()

    responder = Thread(
        target=respond,
        args=(text_queue, queue_event)
    )
    responder.start()

    listener = Listener(
        on_release=on_release_wrapper(text_queue, queue_event),
    )
    listener.daemon = True
    listener.start()


if __name__ == '__main__':
    main()
