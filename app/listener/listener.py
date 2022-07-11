from app.listener.helper import exit_code
from app.listener.helper import helper
from app.settings import Settings


# puts data (text highlighted on screen) to queue when assigned key is pressed, 
# and pushes exit code to queue on press of esc
def on_release_wrapper(queue, event):
    def on_release(key):
        if key == Settings.exit_key:
            queue.put(exit_code)
            event.set()
        if key == Settings.event_key:
            data = helper()
            queue.put(data)
            event.set()
        return queue
    return on_release
