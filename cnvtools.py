from sys import exit
from json import load
import re
import html

'''В данной ситуации думаю,что приемлимо импортировать только одну функцию из сторонних модулей, 
     так как сам модуль является вспомогательным и небольшим по размеру'''


def raise_exception(message, error_type):
    '''raise exception with print error message'''
    try:
        raise error_type('Incorrect JSON data value')
    except error_type:
        print(message)
        exit()


def to_string(tag, tagbody, tag_params=''):
    '''convert pair tag name and tag body to html view'''
    return '<{0}{2}>{1}</{0}>'.format(tag, html.escape(tagbody), tag_params)


def from_json(path):
    '''load data from json file'''
    with open(path, 'r') as f:
        try:
            data = load(f)
        except ValueError:
            print('Incorrect format of file')
            exit()
    return data


def convert_dict(dictionary, in_list=False):
    '''convert dictionary of values to html view'''
    result_string = ''
    for key, value in dictionary.items():
        if isinstance(value, list):
            result_string += convert_list(value, key)
        else:
            current_tag = main_tag(key)
            if current_tag:
                search_values = parse_key(key)
                tag_params = make_tag_with_params(search_values)
                result_string += to_string(current_tag, value, tag_params)
            else:
                result_string += to_string(key, value)
    return '<li>' + result_string + '</li>' if in_list else result_string


def convert_list(list_of_values, tag=''):
    '''convert list of values to html view'''
    result_string = '<ul>'
    for elem in list_of_values:
        if isinstance(elem, dict):
            result_string += convert_dict(elem, True)
    result_string += '</ul>'
    return '<{}>'.format(tag) + result_string + '</{}>'.format(tag) if tag else result_string


def parse_key(key):
    '''divide tag info into classes and id'''
    search_pattern = re.compile('[#](\D[^.#]+)|[.](\D[^.#]+)')
    search_values = re.findall(search_pattern, key)
    classes, id = [], []
    for elem in search_values:
        if elem[0]:
            id.append(elem[0])
        if elem[1]:
            classes.append(elem[1])
    return {'id': id, 'classes': classes}


# по-хорошему нужно было вытянуть это регулярным выражением как классы и айди
# соответственно для всех новых функций(main_tag, make_tag_with_params) нужны тесты но в задании написано лишь их описать, не тратя на них время
def main_tag(tag):
    ''' identify the main tag among other info'''
    index_point = tag.find('.')
    index_lat = tag.find('#')
    if index_point == -1:
        index_point = float('inf')
    if index_lat == -1:
        index_lat = float('inf')

    if index_point < index_lat:
        spliter = '.'
    else:
        spliter = '#'
    cur_tag = tag.split(spliter)[0]
    if cur_tag == tag:
        return None
    else:
        return cur_tag


def make_tag_with_params(params):
    ''' convert css form of classes view to html form'''
    result_string = ''
    if len(params['id']) > 1:
        raise_exception('More than one id at tag', ValueError)
    for elem in params['id']:
        result_string += ' id="{}"'.format(elem)
    if len(params['classes']) > 0:
        result_string += ' class="'
        for elem in params['classes']:
            result_string += '{} '.format(elem)
        result_string += '"'
    return result_string if result_string else ''
