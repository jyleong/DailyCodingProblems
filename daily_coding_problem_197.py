import unittest

'''
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
'''

def rotate_k(nums, k):

    length = len(nums)
    count = 0
    position = 0
    src_num = nums[0]
    while count < length:
        next_position = (position + k) % length
        next_num = nums[next_position]
        nums[next_position] = src_num
        src_num = next_num
        position = next_position
        count += 1
    return nums

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = [5, 4, 3, 2, 1]
        k = 2
        result = [2, 1, 5, 4, 3]
        self.assertEqual(rotate_k(test, k), result)

    def test_case_2(self):

        test = [5, 4, 3, 2, 1]
        k = 3
        result = [3, 2, 1, 5, 4]
        self.assertEqual(rotate_k(test, k), result)
    
    def test_case_3(self):

        test = [5, 4, 3, 2, 1]
        k = 0
        result = [5, 4, 3, 2, 1]
        self.assertEqual(rotate_k(test, k), result)


if __name__ == '__main__':

    unittest.main()