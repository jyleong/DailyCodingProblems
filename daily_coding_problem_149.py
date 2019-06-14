'''
This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist 
L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
'''

import unittest

class SublistSum(object):
    def __init__(self, arr):
        self.sub_list = arr
        self.sub_sum = [0] * len(self.sub_list)
        for i in range(1, len(self.sub_sum)):
            self.sub_sum[i] = self.sub_sum[i-1] + arr[i-1]

    def sum(self, i, j):
        if j >= len(self.sub_sum):
            end = len(self.sub_sum) - 1
            return self.sub_sum[end] - self.sub_sum[i] + self.sub_list[-1]
        return self.sub_sum[j] - self.sub_sum[i]

class DailyCodingProblemsTest(unittest.TestCase):

    def test_case_1(self):
        sum_list = SublistSum([1, 2 ,3, 4, 5])
        result = 5
        
        self.assertEqual(sum_list.sum(1, 3), result)

    def test_case_2(self):
        sum_list = SublistSum([1, 2 ,3, 4, 5])
        result = 6
        
        self.assertEqual(sum_list.sum(0, 3), result)

    def test_case_3(self):
        sum_list = SublistSum([1, 2 ,3, 4, 5])
        result = 9
        self.assertEqual(sum_list.sum(1, 4), result)

    def test_case_4(self):
        sum_list = SublistSum([1, 2 ,3, 4, 5])
        result = 14
        self.assertEqual(sum_list.sum(1, 5), result)

    def test_case_5(self):
        sum_list = SublistSum([1, 2 ,3, 4, 5])
        result = 0
        
        self.assertEqual(sum_list.sum(0, 0), result)

    def test_case_6(self):
        sum_list = SublistSum([1, 2 ,3, 4, 5])
        result = 15
        
        self.assertEqual(sum_list.sum(0, 7), result)


if __name__ == '__main__':
    unittest.main()