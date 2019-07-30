'''
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

'''

import unittest

def can_jump(nums):
    if not nums or len(nums) == 0:
        return True
    cur_idx = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= cur_idx:
            cur_idx = i
    return cur_idx == 0

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [1, 3, 1, 2, 0, 1]
        self.assertTrue(can_jump(test))

    def test_case_2(self):
        test = [1, 2, 1, 0, 0]
        self.assertFalse(can_jump(test))

    def test_case_3(self):
        test = []
        self.assertTrue(can_jump(test))

if __name__ == '__main__':
    unittest.main()


