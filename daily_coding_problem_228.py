'''
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.
'''

import unittest
def comparator(a, b):

    str_ab = str(a) + str(b)
    str_ba = str(b) + str(a)

    return (int(str_ba) > int(str_ab)) - (int(str_ba) < int(str_ab))

class CompareObj(int):
    def __gt__(a, b):
        return comparator(a, b) > 0
    def __lt__(a, b):
        return comparator(a, b) < 0
    def __eq__(a, b):
        return comparator(a, b) == 0
    def __le__(a, b):
        return comparator(a, b) <= 0
    def __ge__(a, b):
        return comparator(a, b) >= 0
    def __ne__(a, b):
        return comparator(a, b) != 0

def largest(nums):
    sorted_comparison = ''.join(sorted(map(str, nums), key=CompareObj))
    return int(sorted_comparison)


class Daily_Coding_Problem_Test(unittest.TestCase):

    def test_case_1(self):

        actual = largest([10, 7, 76, 415])
        expected = 77641510
        self.assertEqual(actual, expected)

    def test_case_2(self):
        actual = largest([10, 2])
        expected = 210
        self.assertEqual(actual, expected)

    def test_case_3(self):
        actual = largest([3, 30, 34, 5, 9])
        expected = 9534330
        self.assertEqual(actual, expected)

if __name__ == '__main__':

    unittest.main()
