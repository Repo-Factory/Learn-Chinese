import requests, bs4


url = 'https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define='


forbidden_characters = [']', '[', '、', '!', '？', '>', '<', '|', '?', ' ', ':', '@', '#', '$', '%', '^', '&', '*',
                            '+', '_', '-', '{', '}',  '(', ')','=', "'", '。', '，', ',', '.', 'A', 'B', 'C', 'D', 'E',
                            'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                            'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '0']


def error_free(character):
    forbidden_characters_list = forbidden_characters
    for forbidden_character in forbidden_characters_list:
        if forbidden_character in str(character):
            return False
    if not verify_html(character):
        return False
    return True


def verify_html(character):
    verified = True
    html = requests.get(f'{url}{character}')
    try:
        html.raise_for_status()
    except Exception as exc:
        verified = False
    return verified


def request_html(character):
    html = requests.get(f'{url}{character}')
    try:
        html.raise_for_status()
    except Exception as exc:
        print(f'Add {character} to list of forbidden characters')
        pass
    return html


def parse_html(html):
    parsed_html = bs4.BeautifulSoup(html.text, 'lxml')
    desired_html = parsed_html.findAll(lambda tag: tag.name == 'div' and tag.get('class') == ['meaning'])
    #test_desired_html = parsed_html.findAll(lambda tag: tag.name == 'span' and tag.get('class') == ['pinyin'])
    #desired_html = parsed_html.findAll(lambda tag: tag.name == 'div' and tag.get('class') == ['definition'])
    return desired_html


def choose_tag(tag_list, pinyin):
    for tag in tag_list:
        if tag.__contains__(f'\n{pinyin}\n'):
            return tag


def get_definitions(desired_html):
    text_list = []
    for html_tag in desired_html[0:2]:
        text = html_tag.getText()
        text_list.append(text)
    return text_list


def format_commas(definitions_string):
    final_string_list = []
    final_string = ''
    for definition in definitions_string:
        definition = definition.replace('\n', ', ')
        final_string_list.append(definition)
    for string in final_string_list:
        if string != final_string_list[-1]:
            final_string += string + ', '
        else:
            final_string += string
    return final_string


def limit_definitions(definitions_string):
    final_string_commas_index = []
    final_string = definitions_string
    for pos, char in enumerate(final_string):
        if char == ',':
            final_string_commas_index.append(pos)
    try:
        final_string = final_string[0:final_string_commas_index[1]]
    except Exception as exc:
        pass
        try:
            final_string = final_string[0:final_string_commas_index[0]]
        except Exception as exc:
            pass
    #        try:
    #            final_string = final_string[0:final_string_commas_index[0]]
    #        except Exception as exc:
    #            return final_string
    return final_string


def format_definition(definitions):
    final_string = format_commas(definitions)
    final_string = limit_definitions(final_string)
    return final_string


def webscrape(character):
    html = request_html(character)
    desired_html = parse_html(html)
    text_list = get_definitions(desired_html)
    text = format_definition(text_list)
    return text




