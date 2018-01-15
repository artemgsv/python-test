import unittest
import cnvtools


class Positive(unittest.TestCase):
    known_values = (
        ({'title': 'Artem', 'body': 'something#1'}, '<h1>Artem</h1><p>something#1</p>'),
        ({}, '')
    )

    tags_to_string_values = (
        (('h1', 'body'), '<h1>body</h1>'),
        (('p', 'Go'), '<p>Go</p>')
    )

    def test_convert_dict(self):
        ''' convert dictionary to html'''
        for data, result in self.known_values:
            self.assertEqual(cnvtools.convert_dict(data, ('h1', 'p')), result)

    def test_to_string(self):
        for tags, result in self.tags_to_string_values:
            self.assertEqual(cnvtools.to_string(tags[0], tags[1]), result)


class BadInput(unittest.TestCase):
    def test_empty_dict(self):
        '''convert empty dictionary'''
        self.assertRaises(ValueError, cnvtools.convert_dict, {})



    if __name__ == '__main__':
        unittest.main()

