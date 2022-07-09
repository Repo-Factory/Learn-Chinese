from translator.translator import process_text


def main(queue, event):
    while True:
        event.wait()
        if queue.empty() is False:
            string = queue.get()
            if string == 'exit code: FC789456':
                exit()
            else:
                process_text(string)
            event.clear()
