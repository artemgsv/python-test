from sys import exit
from json import load
import re
import html
import custom_exception

'''В данной ситуации думаю,что приемлимо импортировать только одну функцию из сторонних модулей, 
     так как сам модуль является вспомогательным и небольшим по размеру'''


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
                try:
                    tag_params = make_tag_with_params(search_values)
                except custom_exception.CountIdError:
                    print('Expect one id in html tag, but allowed more')
                    exit()
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


def main_tag(tag):
    ''' identify the main tag among other info'''
    tag_info = re.split('[.#]', tag)
    current_tag = tag_info[0] if tag_info[0] != tag else None
    return current_tag


def make_tag_with_params(params):
    ''' convert css form of classes view to html form'''
    result_string = ''
    if len(params['id']) > 1:
        raise custom_exception.CountIdError()
    for elem in params['id']:
        result_string += ' id="{}"'.format(elem)
    if len(params['classes']) > 0:
        result_string += ' class="'
        for elem in params['classes']:
            result_string += '{} '.format(elem)
        result_string += '"'
    return result_string if result_string else ''
