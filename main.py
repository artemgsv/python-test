from jsoncnv import JsonConverter

a = JsonConverter('source.json', ('h1', 'p'))
a.convert_to_html()