'''This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?'''
import unittest

def find_once(arr):
    xor = 0
    for num in arr:
        xor ^= num
    xor = xor & ~(xor-1)
    answer_1 = 0
    answer_2 = 0
    for num in arr:
        if (xor & num > 0):
            answer_1 ^= num
        else:
            answer_2 ^= num

    return (answer_1, answer_2)

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test_case = [2, 4, 6, 8, 10, 2, 6, 10]
        result = (4, 8)
        
        self.assertEqual(find_once(test_case), result)

    def test_case_2(self):

        test_case = [0, 7, 9, 0, 1, 7 ,5, 1]
        result = (5, 9)
        self.assertEqual(find_once(test_case), result)



if __name__ == '__main__':

    unittest.main()