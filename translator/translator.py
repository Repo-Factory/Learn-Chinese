from chinese import ChineseAnalyzer
import pinyin


def parse_text(queue, event):
    analyzer = ChineseAnalyzer()
    while True:
        event.wait()
        if queue.empty() is False:
            string = queue.get()
            event.clear()
            parsed_text = analyzer.parse(string)
            for token in parsed_text.tokens():
                print(pinyin.get(token))

    # print(result.pinyin())



