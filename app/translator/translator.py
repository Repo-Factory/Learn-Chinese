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
        try:
            translation = translator.translate(string, src='zh-tw', dest='en').text
        except Exception as exc:
            translation = ''
    return translation


# gives 2nd (or more) translation(s) for each word (token combination) by webscraping
def translate(character, num_definitions):
    if character == '了':   # some abstract words have terrible translations online; 
                            # ideally I would have a database for common words that  
                            # are incorrectly translated where definitions could be  
                            # retrieved but for now I just have a collection of
                            # if statements for ones that have bothered me 
        translation = 'Particle indicating action has taken place'
    else:
        translation = webscrape(character, num_definitions)
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
            translations = translate(character, Settings.desired_translations)
            google_translation = request_google(character)
            print(f'{character}  -  {pinyin_text}  -  {google_translation} | {translations}\n')
    print('\n\n\n translation complete....')

