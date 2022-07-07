import requests, bs4


url = 'https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define='


chinese_characters = '喜欢'


def request_html(character):
    html = requests.get(f'{url}{character}')
    try:
        html.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % exc)
        pass
    return html


def parse_html(html):
    parsed_html = bs4.BeautifulSoup(html.text, 'lxml')
    desired_html = parsed_html.findAll(lambda tag: tag.name == 'div' and tag.get('class') == ['meaning'])
    return desired_html


def get_text(desired_html):
    text_list = []
    for html_tag in desired_html[0:2]:
        text = html_tag.getText()
        text_list.append(text)
    return text_list


def format_definition(definitions):
    final_string_list = []
    final_string = ''
    for definition in definitions:
        definition = definition.replace('\n', ', ')
        final_string_list.append(definition)
    for string in final_string_list:
        if string != final_string_list[-1]:
            final_string += string + ', '
        else:
            final_string += string
    return final_string


def webscrape(character):
    html = request_html(character)
    desired_html = parse_html(html)
    text_list = get_text(desired_html)
    text = format_definition(text_list)
    return text


print(webscrape(chinese_characters))