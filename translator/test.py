from webscraper import request_html
from webscraper import parse_html
from webscraper import get_definitions
from webscraper import choose_tag
from webscraper import format_definition
from webscraper import format_commas
from webscraper import limit_definitions
url = 'https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define='


def test_format_definitions(definitions):
    if definitions is None:
        text = ''
    else:
        text = definitions.replace('\n', ', ')
    text_commas_index = []
    for pos, char in enumerate(text):
        if char == ',':
            text_commas_index.append(pos)
    try:
        final_string = text[text_commas_index[1] + 2: text_commas_index[-1]]
    except Exception as exc:
        final_string = ''
    return final_string


def test_webscrape(character, pinyin_text):
    html = request_html(character)
    desired_html = parse_html(html)
    text_list = get_definitions(desired_html)
    tag = choose_tag(text_list, pinyin_text)
    text = test_format_definitions(tag)
    return text


test_html = request_html('领域')

parsed = parse_html(test_html)

definitions = get_definitions(parsed)

print(definitions)


text = choose_tag(definitions, 'Lǐng yù')
if text is None:
    text = ''

print(text)

text = text.replace('\n' , ', ')


text_commas_index= []
for pos, char in enumerate(text):
    if char == ',':
        text_commas_index.append(pos)
try :
    final_string = text[text_commas_index[1] + 2: text_commas_index[-1]]
except Exception as exc:
    final_string = ''

print(final_string)


