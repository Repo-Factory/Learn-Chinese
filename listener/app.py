from pynput.keyboard import Listener
from listener.helperTwo import on_release
import threading
from learner.learnerTwo import parse_text


translator_thread = threading.Thread (
    target=parse_text,
    args=('我很高兴认识你',)
    )
translator_thread.start()
translator_thread.join()


# Continual listening process
with Listener(
       on_release=on_release,
       ) as listener:
    listener.join()