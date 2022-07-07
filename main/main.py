from translator.translator import process_text
from translator.translator import create_analyzer


analyzer = create_analyzer()


def main(queue, event):
    while True:
        event.wait()
        if queue.empty() is False:
            string = queue.get()
            process_text(string, analyzer)
            event.clear()
