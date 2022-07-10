from translator.translator import process_text
from listener.helper import exit_code


# waits for information to enter queue... when it does, it either exits or sends the text to be processed
def main(queue, event):
    while True:
        event.wait()
        if queue.empty() is False:
            string = queue.get()
            if string == exit_code:
                exit()
            else:
                process_text(string)
            event.clear()
