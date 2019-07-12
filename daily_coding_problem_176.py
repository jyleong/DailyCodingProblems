'''
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
'''

import unittest

def one_to_one(s1, s2):
    if not s1 and not s2:
        return True
    if not s1 or not s2 or (len(s1) != len(s2)):
        return False
    
    visited_chars = set()

    mapping = dict()

    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 not in mapping and c2 not in visited_chars:
            mapping[c1] = c2
            visited_chars.add(c2)
        elif c1 not in mapping and c2 in visited_chars:
            return False
        elif mapping[c1] != c2:
            return False
    return True

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        s1 = 'abc'
        s2 = 'bcd'

        self.assertTrue(one_to_one(s1, s2))

    def test_case_2(self):
        s1 = 'foo'
        s2 = 'bar'

        self.assertFalse(one_to_one(s1, s2))

    def test_case_3(self):
        s1 = 'bar'
        s2 = 'foo'

        self.assertFalse(one_to_one(s1, s2))

    def test_case_4(self):
        s1 = ''
        s2 = 'bcd'

        self.assertFalse(one_to_one(s1, s2))



if __name__ == '__main__':

    unittest.main()

