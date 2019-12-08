'''
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

'''

import unittest

def not_smallest_subset(nums):
    result = 1
    for n in nums:
        if n > result:
            return result
        else:
            result += n
    return result

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = [1, 2, 3, 10]
        expected = 7
        actual = not_smallest_subset(test)

        self.assertEquals(actual, expected)

    def test_case_2(self):

        test = [5, 6, 7, 10]
        expected = 1
        actual = not_smallest_subset(test)

        self.assertEquals(actual, expected)

    def test_case_3(self):

        test = [1, 2, 3, 4, 6, 10]
        expected = 27
        actual = not_smallest_subset(test)

        self.assertEquals(actual, expected)

if __name__ == '__main__':

    unittest.main()


