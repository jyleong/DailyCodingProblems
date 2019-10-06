'''
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
'''

import unittest

ROMAN_MAP = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I':1
        }

def roman_to_decimal(roman):
    decimal = 0
    if not roman or len(roman) == 0:
        return decimal

    prev_char = None
    for c in roman:
        value = ROMAN_MAP.get(c)
        if prev_char is not None:
            if value > prev_char:
                decimal -= prev_char
                decimal += value - prev_char
                prev_char = None
            else:
                decimal += value
        else:
            decimal += value
        prev_char = value

    return decimal

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = 'XIV'
        expected = 14
        actual = roman_to_decimal(test)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        test = 'IV'
        expected = 4
        actual = roman_to_decimal(test)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        test = 'XC'
        expected = 90
        actual = roman_to_decimal(test)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        test = 'VIII'
        expected = 8
        actual = roman_to_decimal(test)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        test = 'MDCXV'
        expected = 1615
        actual = roman_to_decimal(test)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        test= 'XLVI'
        expected = 46
        actual = roman_to_decimal(test)
        self.assertEqual(actual, expected)



if __name__ == '__main__':

    unittest.main()
