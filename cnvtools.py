from sys import exit
from json import load
'''  В данной ситуации думаю,что приемлимо импортировать только одну функцию из сторонних модулей, 
     так как сам модуль является вспомогательным и небольшим по размеру
'''

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
        except ValueError as e:
            print('Incorrect format of file')
            exit()
    return data


def convert_dict(dict, config=('head', 'body')):
    '''convert dictionary of values to html view'''
    count = 0
    str = ''
    for key, value in dict.items():
        if config[count]:
            str += to_string(config[count], value)
        count += 1
    return str
