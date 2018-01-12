import cnvtools

'''
    Для первой задачи было решено завести типаж (так называемый конфиг), для того чтобы предусмотреть поведение по умолчанию
    В случае требования заказчика изменить теги, например на h2 и article, это будет полезно
    
    Для первой задачи не указано много различных моментов, таких как поведение при пустом листе, словаре, отсутствии ключа,
    другого названия ключа, при записи значений из словаря, поэтому все они обрабатываются как ошибка
'''


class JsonConverter:
    ''' class for converting json to html by rules'''

    def __init__(self, path, config=('head', 'body')):
        self.data = cnvtools.from_json(path)
        self.config = config

    def convert_to_html(self):
        '''convert data from json to html'''
        if type(self.data) is list and len(self.data) > 0:
            for elem in self.data:
                if len(elem) != 2:  # в задаче не указано поведение при наличии более двух элементов в словаре
                    '''
                        Здесь нужно было бы еще проверять правильность ключей (то есть соответствие их 'title' и 'body'
                        Но будем считать, что их правильность гарантируется, чтобы не награмождать код лишними проверками 
                    
                    '''
                    cnvtools.raise_exception('Incorrect JSON data value', ValueError)
                print(cnvtools.convert_dict(elem, self.config))
        else:
            cnvtools.raise_exception('Incorrect format of data in file',ValueError)
            # не указано что делать в случае если json данные являются словарем, не завернутым в список
