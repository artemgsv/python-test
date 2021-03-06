import cnvtools
import custom_exception
'''Для первой задачи было решено завести типаж (так называемый конфиг), для того чтобы предусмотреть поведение по умолчанию
    В случае требования заказчика изменить теги, например на h2 и article, это будет полезно
    Для первой задачи не указано много различных моментов, таких как поведение при пустом листе, словаре, отсутствии ключа,
    другого названия ключа, при записи значений из словаря, поэтому все они обрабатываются как ошибка'''


class JsonConverter:
    ''' class for converting json to html by rules'''

    def __init__(self, path):
        self.data = cnvtools.from_json(path)

    def convert_to_html(self):
        '''convert data from json to html'''
        if isinstance(self.data, list) and len(self.data) > 0:
            print(cnvtools.convert_list(self.data))
        elif isinstance(self.data, dict) and len(self.data) > 0:
            print(cnvtools.convert_dict(self.data))
        else:
            raise custom_exception.JsonFormatError('Json data is invalid')
