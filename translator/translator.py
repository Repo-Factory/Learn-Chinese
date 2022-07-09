from chinese import ChineseAnalyzer
import pinyin
from translator.webscraper import webscrape
from translator.webscraper import test_webscrape
from googletrans import Translator
from translator.webscraper import error_free

translator = Translator()
analyzer = ChineseAnalyzer()


def request_google(string):
    try:
        translation = translator.translate(string).text
    except Exception as exc:
        try:
            translation = translator.translate(string, src='zh-tw', dest='en').text
        except Exception as exc:
            translation = ''
    return translation


def parse_text(string):
    parsed_text = analyzer.parse(string)
    return parsed_text.tokens()


def translate(character):
    translation = webscrape(character)
    return translation


def process_text(string):
    print(request_google(string))
    token_list = parse_text(string)
    for token in token_list:
        if not error_free(token) or token is None or token == ' ' or '\n' in token or token == '':
            continue
        else:
            character = token
            pinyin_text = pinyin.get(token)
            translation = translate(character)
            google_translation = request_google(character)
            print(f'{character}  -  {pinyin_text}  -  {translation} | {google_translation}')


