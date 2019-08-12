'''
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
'''

import unittest

def permute(nums, P):
    if not nums or not P or len(nums) == 0 or len(P) == 0:
        raise Exception('Invalid Input')

    idx_dict = dict()
    for i in range(len(nums)):
        idx_dict[i] = nums[i]

    for i in range(len(P)):
        nums[i] = idx_dict[P[i]]
    return nums

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = ['a', 'b', 'c']
        P = [2, 1, 0]
        result = ['c', 'b', 'a']
        self.assertEqual(permute(test, P), result)

    def test_case_2(self):
        test = []
        P = [2, 1, 0]
        self.assertRaises(Exception, permute, test, P)

    def test_case_3(self):

        test = ['a', 'b', 'c', 'd', 'e']
        P = [1, 2, 0, 4, 3]
        result = ['b', 'c', 'a', 'e', 'd']

if __name__ == '__main__':

    unittest.main()




