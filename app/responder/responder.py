from app.translator.translator import process_text
from app.listener.helper import exit_code
from app.listener.helper import close_page_string


# waits for information to enter queue... when it does, it either exits or sends the text to be processed
def respond(queue, event):
    while True:
        event.wait()
        if queue.empty() is False:
            string = queue.get()
            if string == exit_code:
                print(close_page_string)
                exit()
            else:
                process_text(string)
            event.clear()
