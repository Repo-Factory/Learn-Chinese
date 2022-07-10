import requests, bs4


url = 'https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define='


forbidden_characters = [']', '[', '、', '!', '？', '>', '<', '|', '?', ' ', ':', '@', '#', '$', '%', '^', '&', '*',
                            '+', '_', '-', '{', '}',  '(', ')','=', "'", '。', '，', ',', '.', 'A', 'B', 'C', 'D', 'E',
                            'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                            'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '0']


# translate online continues if pages exists and the input is chinese (not forbidden)
def error_free(character):
    forbidden_characters_list = forbidden_characters
    for forbidden_character in forbidden_characters_list:
        if forbidden_character in str(character):
            return False
    if not verify_html(character):
        return False
    return True


# makes request to site with specific character, if page doesn't exist, translation will not continue
def verify_html(character):
    verified = True
    html = requests.get(f'{url}{character}')
    try:
        html.raise_for_status()
    except Exception as exc:
        verified = False
    return verified


# returns html page or error message
def request_html(character):
    html = requests.get(f'{url}{character}')
    try:
        html.raise_for_status()
    except Exception as exc:
        print(f'Add {character} to list of forbidden characters')
        pass
    return html


# beautiful soup parses html
def parse_html(html):
    parsed_html = bs4.BeautifulSoup(html.text, 'lxml')
    return parsed_html


# takes in info of specific tag that wants to be scraped and returns those tags
def produce_tags(parsed_html, tag_type, tag_get, tag_name):
    tag_list = []
    needed_tags = parsed_html.findAll(lambda tag: tag.name == f'{tag_type}' and tag.get(f'{tag_get}') == [f'{tag_name}'])
    for needed_tag in needed_tags:
        tag_list.append(needed_tag.text)
    return tag_list


# specific to yabla page, formats strings based on how they are presented in the html,
# returns one string with words separated only by commas and a space
def format_translation_yabla(tag_list):
    formatted_tag_list = []
    for tag in tag_list:
        tag_string = tag.replace('\n', ', ')
        formatted_tag_list.append(tag_string)
    return ', '.join(formatted_tag_list)


# cuts string down to the number of definitions desired, passed in in parse_text
def limit_string(string, string_number):
    commas_index = []
    for pos, char in enumerate(string):
        if char == ',':
            commas_index.append(pos)
    string_produced = False
    i = string_number
    while string_produced is False and i > 0:
        try:
            string = string[0: commas_index[i - 1]]
            string_produced = True
        except Exception as exc:
            i = i - 1
    return string


# calls all related webscraping functions
def webscrape(character, string_number):
    html = request_html(character)
    parsed_html = parse_html(html)
    tags = produce_tags(parsed_html, 'div', 'class', 'meaning')
    translations = format_translation_yabla(tags)
    translation = limit_string(translations, string_number)
    return translation






