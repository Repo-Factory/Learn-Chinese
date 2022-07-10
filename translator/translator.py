from chinese import ChineseAnalyzer
import pinyin
from translator.webscraper import webscrape
from googletrans import Translator
from translator.webscraper import error_free


translator = Translator()  # google translate object
analyzer = ChineseAnalyzer()  # chinese package object


# words in chinese can be multiple characters, chinese package
# has a parser to split into the most likely combination of words
def parse_text(string):
    parsed_text = analyzer.parse(string)
    return parsed_text.tokens()


# makes request to google translate API for translation
def request_google(string):
    try:
        translation = translator.translate(string).text
    except Exception as exc:
        try:
            translation = translator.translate(string, src='zh-tw', dest='en').text
        except Exception as exc:
            translation = ''
    return translation


# gives 2nd translation for each word (token combination) by webscraping
def translate(character):
    translation = webscrape(character)
    return translation


# gathers character, pinyin, and multiple english translations and prints them to the screen with appropriate spacing
def process_text(string):
    print(request_google(string))
    print('\n')
    token_list = parse_text(string)
    for token in token_list:
        if not error_free(token) or token is None or token == ' ' or '\n' in token or token == '':
            continue
        else:
            character = token
            pinyin_text = pinyin.get(token)
            translations = webscrape(character, 1)
            google_translation = request_google(character)
            print(f'{character}  -  {pinyin_text}  -  {google_translation} | {translations}\n')


