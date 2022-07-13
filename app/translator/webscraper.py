import requests, bs4
from app.settings import Settings

# URL needed to check if chinese character exists in verify_html 
# (I also use it for the web scrape but the webscrape function can adapt to a different site)
error_validation_url = 'https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define='


forbidden_characters = [']', '[', '、', '!', '？', '>', '<', '|', '?', ' ', ':', '@', '#', '$', '%', '^', '&', '*',
                            '+', '_', '-', '{', '}',  '(', ')','=', "'", '。', '，', ',', '.', 'A', 'B', 'C', 'D', 'E',
                            'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                            'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '0']


# translate online continues if pages exists and the character is chinese (not forbidden)
def error_free(character):
    forbidden_characters_list = forbidden_characters
    for forbidden_character in forbidden_characters_list:
        if forbidden_character in str(character):
            return False
    if not verify_html(error_validation_url, character):
        return False
    return True


# makes request to site with specific character, if page doesn't exist, translation will not continue
def verify_html(url, character):
    verified = True
    html = requests.get(f'{url}{character}')
    try:
        html.raise_for_status()
    except Exception as exc:
        verified = False
    return verified


# returns html page or error message (if new forbidden character encountered) for url page of specific character
def request_html(url, character):
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
def produce_tags(parsed_html, tag_type, tag_attr, tag_name):
    tag_list = []
    needed_tags = parsed_html.findAll(lambda tag: tag.name == f'{tag_type}' and tag.get(f'{tag_attr}') == [f'{tag_name}'])
    for needed_tag in needed_tags:
        tag_list.append(needed_tag.text)
    return tag_list


# General formatting function for strings to clean up how they are presented in the html,
# returns one string with words separated only by commas and a space. This function does an
# okay job for general cleaning but it's best to use a custom function made in settings.py
# to make the formatting specific to how the tags come out for the specific webscrape
def format_translations(tag_list):
    formatted_tag_list = []
    for tag in tag_list:
        tag_string = tag.replace('\n', ' ')
        tag_string = tag_string.replace(',', ' ')
        tag_string = tag_string.replace('  ', ' ')
        tag_string = tag_string.replace(' ', ', ')
        formatted_tag_list.append(tag_string)
    return ', '.join(formatted_tag_list)

# cuts string down to the number of definitions desired, must be passed a string of words 
# separated by commas to work correctly, so the formatting function is important
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


# actually does webscraping work, calls all related webscraping functions
def webscrape_mule(url, character, tag_type, tag_attr, tag_name, format_translations, string_number):
    html = request_html(url, character)
    parsed_html = parse_html(html)
    tags = produce_tags(parsed_html, f'{tag_type}', f'{tag_attr}', f'{tag_name}')
    formatted_translations = format_translations(tags)
    translation = limit_string(formatted_translations, string_number)
    return translation


# I wanted only the character and desired translation numbers to be passed in the translator
# page, but in case I (or someone else) would like to scrape a different site for definitions
# this is the function where all the necessary values can be changed; a unique formatting
# function will have to be created because not all tag text from beautiful soup html
# will be in the desired format for displaying translations. I put a general format translations
# function at the bottom that works pretty well for most cases, but it can't be perfect, depending
# on the site layout
def webscrape(character, string_number):
    translation = webscrape_mule(
          url=Settings.url,
          character=f'{character}',
          tag_type=Settings.tag_type,
          tag_attr=Settings.tag_attr,
          tag_name=Settings.tag_name,
          format_translations=Settings.format,
          string_number=string_number,
          )
    return translation
