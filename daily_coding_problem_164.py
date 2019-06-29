'''
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
'''

import unittest

def find_dup(arr):
    occured = set()
    for n in arr:
        if n not in occured:
            occured.add(n)
        else:
            return n

def find_dup_2(arr):
    real_len = len(arr)-1
    expected_sum = (real_len * (real_len + 1)) / 2

    actual_sum = sum(arr)
    return actual_sum - expected_sum

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [1, 3, 2, 4, 2, 5]
        result = 2
        self.assertEqual(find_dup(test), result)

    def test_case_2(self):
        test = [1, 3, 2, 4, 7, 5, 6, 3]
        result = 3
        self.assertEqual(find_dup(test), result)

    def test_case_3(self):
        test = [1, 3, 2, 4, 2, 5]
        result = 2
        self.assertEqual(find_dup_2(test), result)

    def test_case_4(self):
        test = [1, 3, 2, 4, 7, 5, 6, 3]
        result = 3
        self.assertEqual(find_dup_2(test), result)

if __name__ == '__main__':
    unittest.main()