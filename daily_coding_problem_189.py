'''
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''
import unittest

def distinct_subarray(nums):
    if not nums or len(nums) == 0:
        return 0

    def distinct_helper(array, seen=set()):
        if not array or len(array) == 0:
            return len(seen)
        if array[0] in seen:
            return len(seen)
        set_copy = seen.copy()
        set_copy.add(array[0])
        with_num = distinct_helper(array[1:], set_copy)
        not_with_num = distinct_helper(array[1:], set())
        return max(with_num, not_with_num)
    return distinct_helper(nums, set())
class DailyCodingProblemTest(unittest.TestCase):
    def test_case_1(self):
        test = [5, 1, 3, 5, 2, 3, 4, 1]
        self.assertEqual(distinct_subarray(test), 5)

    def test_case_2(self):
        test = []
        self.assertEqual(distinct_subarray(test), 0)

    def test_case_3(self):
        test = [5, 1, 3, 5]
        self.assertEqual(distinct_subarray(test), 3)


if __name__ == '__main__':
    unittest.main()

