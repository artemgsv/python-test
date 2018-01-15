from sys import exit
from json import load
'''В данной ситуации думаю,что приемлимо импортировать только одну функцию из сторонних модулей, 
     так как сам модуль является вспомогательным и небольшим по размеру'''


def raise_exception(message, error_type):
    '''raise exception with print error message'''
    try:
        raise error_type('Incorrect JSON data value')
    except error_type:
        print(message)
        exit()


def to_string(tag, tagbody):
    '''convert pair tag name and tag body to html view'''
    return '<{0}>{1}</{0}>'.format(tag, tagbody)


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
