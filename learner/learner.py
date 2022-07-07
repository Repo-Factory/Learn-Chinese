from chinese import ChineseAnalyzer


def parse_text(string):
    analyzer = ChineseAnalyzer()
    parsed_text = analyzer.parse(string)
    print(parsed_text.tokens())
    print(parsed_text.pinyin())