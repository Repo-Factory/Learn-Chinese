from chinese import ChineseAnalyzer
import pinyin
from translator.webscraper import webscrape


def create_analyzer():
    analyzer = ChineseAnalyzer()
    return analyzer


def parse_text(string, analyzer):
    analyzer = analyzer
    parsed_text = analyzer.parse(string)
    return parsed_text.tokens()


def translate(character):
    translation = webscrape(character)
    return translation


def process_text(string, analyzer):
    token_list = parse_text(string, analyzer)
    for token in token_list:
        character = token
        pinyin_text = pinyin.get(token)
        translation = translate(character)
        print(f'{character} - {pinyin_text} - {translation}')