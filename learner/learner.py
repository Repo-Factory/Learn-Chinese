from chinese import ChineseAnalyzer


def parse_text(queue):
    analyzer = ChineseAnalyzer()
    while True:
        if queue.empty() is False:
            string = queue.get()
            parsed_text = analyzer.parse(string)
            print(parsed_text.tokens())
            print(parsed_text.pinyin())
    # print(result.pinyin())



