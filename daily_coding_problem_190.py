'''
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
'''
import unittest

def circular_max_sum(nums):
    if not nums or len(nums) == 0:
        return 0

    result = nums[0]
    length = len(nums)

    for i in range(len(nums)):
        j = 0 if (i+1) % length == 0 else i + 1
        sub_sum_here = nums[i]
        while j != i:

            sub_sum_here += nums[j]
            result = max(result, sub_sum_here)
            if (j+1) % length == 0:
                j = 0
            else:
                j += 1

    return result

class DailyCodingProblemTest(unittest.TestCase):
    def test_case_1(self):
        test = [8, -1, 3, 4]
        result = 15
        self.assertEqual(circular_max_sum(test), result)

    def test_case_2(self):
        test = []
        result = 0
        self.assertEqual(circular_max_sum(test), result)

    def test_case_3(self):
        test = [-4, 5, 1, 0]
        result = 6
        self.assertEqual(circular_max_sum(test), result)



if __name__ == '__main__':
    unittest.main()
