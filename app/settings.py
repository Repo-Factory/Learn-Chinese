from pynput.keyboard import Key


class Settings:
    desired_translations = 1
    event_key = Key.alt_l      # key to copy highlight text
    exit_key = Key.esc

    def format_translations_yabla(tag_list): # used by webscraper to format, if webscrape url changed,
        formatted_tag_list = []              # formatting will need editing
        for tag in tag_list:
            tag_string = tag.replace('\n', ', ')
            formatted_tag_list.append(tag_string)
        return ', '.join(formatted_tag_list)

    # webscrape details
    url = 'https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define='
    tag_type = 'div'
    tag_attr = 'class'
    tag_name = 'meaning'
    format = format_translations_yabla


