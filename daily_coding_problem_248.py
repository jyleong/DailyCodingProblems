'''
This problem was asked by Nvidia.

Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
'''

import unittest

'''
5 - 1 / 2= 4 / 2
1/5 = 0.2
5/1 = 5
binary = 5 + 1 / 2 = 3

15 - 6 = 9 / 2 = 4.5
21 / 2 = 10.5
'''
def find_max(a, b):

    diff = abs(b-a) / 2
    add = (b + a) / 2
    return int(add + diff)

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        actual = find_max(15, 6)
        self.assertEqual(15, actual)

    def test_case_2(self):
        actual = find_max(221, 400)
        self.assertEqual(400, actual)

    def test_case_3(self):
        actual = find_max(1, 5)
        self.assertEqual(5, actual)

if __name__ == '__main__':

    unittest.main()

