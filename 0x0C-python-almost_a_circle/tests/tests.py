#!/usr/bin/python
"""Class and methods used to test and vaidate PEP8 files"""
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """This function turn the data to upper case"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        """This function two string"""
        data = 'Tom Jackson'
        self.assertEqual(data.split(), ['Tom', 'Jackson'])
        with self.assertRaises(TypeError):
            data.split(2)


if __name__ == '__main__':
    unittest.main()
