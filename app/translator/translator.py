from chinese import ChineseAnalyzer
import pinyin
from googletrans import Translator
from app.translator.webscraper import error_free
from app.translator.webscraper import webscrape
from app.settings import Settings


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
        translation = ''
    return translation


# gives 2nd (or more) translation(s) for each word (token combination) by webscraping
def translate(character, num_definitions):
    character_list = { '了' : 'Particle indicating action has taken place',
                       '有' : 'There are/is',
                       '我' : 'I',               # list of common connecter words that 
                     }                           # don't translate well online
    if character in character_list:
        translation = character_list[character]
    else:
        translation = webscrape(character, num_definitions)
    return translation


# gathers character, pinyin, and multiple english translations and prints them to the screen with appropriate spacing
def process_text(string):
    print_full_trans(string)        # prints full translation before word-for-word
    token_list = parse_text(string)
    for token in token_list:
        if not error_free(token) or token is None or token == ' ' or token == '' or '\n' in token:
            continue
        else:
            character = token
            pinyin_text = pinyin.get(token)
            translations = translate(character, Settings.desired_translations)
            google_translation = request_google(character)
            print(f'{character}  -  {pinyin_text}  -  {google_translation} | {translations}\n')
    print_complete()


# print helpers
def print_full_trans(string):
    print(request_google(string))
    print('\n')


def print_complete():
    print('\n\n\n translation complete....')