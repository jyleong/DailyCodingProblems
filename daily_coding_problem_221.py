'''
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.
'''

import unittest

def get_nth_sevenish(n):
    if n < 1:
        raise Exception('Invalid number for n')

    sevens = []
    i = 0
    while len(sevens) < n:
        new_pow = 7 ** i
        sevens.append(new_pow)
        new_arr = [num + new_pow for num in sevens]
        sevens += new_arr

    return sevens[n-1]

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        number = 1
        expected = 1
        self.assertEqual(expected, get_nth_sevenish(number))

    def test_case_2(self):
        number = 2
        expected = 7
        self.assertEqual(expected, get_nth_sevenish(number))

    def test_case_3(self):
        number = 4
        expected = 49
        self.assertEqual(expected, get_nth_sevenish(number))

    def test_case_4(self):
        number = 11
        expected = 358
        self.assertEqual(expected, get_nth_sevenish(number))

    def test_case_5(self):
        number = 0
        self.assertRaises(Exception, get_nth_sevenish, number)
