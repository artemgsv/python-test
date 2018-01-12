import unittest
import cnvtools


class Positive(unittest.TestCase):
    known_values = (
        ({'title': 'Artem', 'body': 'something#1'}, '<h1>Artem</h1><p>something#1</p>'),
        ({}, '')
    )

    def test_convert_dict(self):
        ''' convert dictionary to html'''
        for data, result in self.known_values:
            self.assertEqual(cnvtools.convert_dict(data, ('h1', 'p')), result)


class BadInput(unittest.TestCase):
    def test_empty_dict(self):
        '''convert empty dictionary'''
        self.assertRaises(ValueError, cnvtools.convert_dict, {})

    def test_invalid_json_format(self):
        self.assertRaises(ValueError, cnvtools.convert_dict, {[{}]})


    if __name__ == '__main__':
        unittest.main()

