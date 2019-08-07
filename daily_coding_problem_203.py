'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
'''

import unittest

def find_min(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + ((right - left)//2)

        if arr[left] <= arr[mid] and arr[right] < arr[mid]:
            left = mid + 1
        elif arr[left] >= arr[mid] and arr[right] > arr[mid]:
            right = mid - 1
        elif arr[left] <= arr[mid] and arr[right] > arr[mid]:
            return arr[left]
        elif arr[left] > arr[mid] and arr[right] < arr[mid]:
            return arr[right]
    return arr[left]

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = [5, 7, 10, 3, 4]
        result = 3
        self.assertEqual(find_min(test), result)

    def test_case_2(self):

        test = [7, 10, 1, 2, 3, 4, 6, 7]
        result = 1
        self.assertEqual(find_min(test), result)

    def test_case_3(self):
        test = [4, 5, 7, 10, 3]
        result = 3
        self.assertEqual(find_min(test), result)

if __name__ == '__main__':

    unittest.main()

