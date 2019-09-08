'''
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

'''

import unittest

def get_spreadsheet_col(number):
    result = ''
    CHARMAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while number > 0:
        if number % 26 == 0:
            result = CHARMAP[25] + result
            number = number // 26 - 1
        else:
            val = number % 26 - 1
            result = CHARMAP[val] + result
            number = number // 26

    return result



class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = 1
        result = 'A'
        self.assertEqual(get_spreadsheet_col(test), result)

    def test_case_2(self):
        test = 27
        result = 'AA'
        self.assertEqual(get_spreadsheet_col(test), result)

    def test_case_3(self):
        test = 51
        result = 'AY'
        self.assertEqual(get_spreadsheet_col(test), result)

    def test_case_4(self):
        test = 26
        result = 'Z'
        self.assertEqual(get_spreadsheet_col(test), result)

    def test_case_5(self):
        test = 700
        result = 'ZX'
        self.assertEqual(get_spreadsheet_col(test), result)

    def test_case_6(self):
        test = 676
        result = 'YZ'
        self.assertEqual(get_spreadsheet_col(test), result)

    def test_case_7(self):
        test = 705
        result = 'AAC'
        self.assertEqual(get_spreadsheet_col(test), result)

if __name__ == '__main__':

    unittest.main()
