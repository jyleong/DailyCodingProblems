'''
This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
'''

import unittest

def strip_neg(str):
    if (str[0] == '-'):
        return str[1:]
    return str

def is_valid(str):
    if not str:
        return True

    is_dec = False

    # iter over each char
    for i in range(len(str)):
        c = str[i]
        if (not c.isdigit() and c != '.') or (c == '.' and is_dec):
            return False
        if (c == '.' and not is_dec):
            is_dec = True
    return True


def repr_number(input):
    if not input or len(input) == 0:
        return False

    # split by 'e' if exists
    chunks = input.split('e')
    # too many e
    if (len(chunks) > 2):
        return False

    if (len(chunks) == 2):
        # verify case for both halves
        return chunks[0] and chunks[1] and is_valid(chunks[0]) and is_valid(chunks[1])

    else:
        # cleanse negative
        #do check on each char
        cleanse_str = strip_neg(chunks[0])
        return cleanse_str and is_valid(cleanse_str)

class Daily_Coding_Problem_Test(unittest.TestCase):

    def test_case_1(self):
        input = "10"
        self.assertTrue(repr_number(input))

    def test_case_2(self):
        input = "-10"
        self.assertTrue(repr_number(input))

    def test_case_3(self):
        input = "10.1"
        self.assertTrue(repr_number(input))

    def test_case_4(self):
        input = "-10.1"
        self.assertTrue(repr_number(input))

    def test_case_5(self):
        input = "1e5"
        self.assertTrue(repr_number(input))

    def test_case_6(self):
        input = "a"
        self.assertFalse(repr_number(input))

    def test_case_7(self):
        input = "x 1"
        self.assertFalse(repr_number(input))

    def test_case_8(self):
        input = "a -2"
        self.assertFalse(repr_number(input))

    def test_case_9(self):
        input = "-"
        self.assertFalse(repr_number(input))
        

if __name__ == "__main__":

    unittest.main()


