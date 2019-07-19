'''
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
'''
import unittest

def solution(array):
    if not array or len(array) < 1:
        raise RuntimeError('Invalid Input')

    result = array[0]
    for i in range(1, len(array)):
        if result < array[i]:
            result = gcd(array[i], result)
        else:
            result = gcd(result, array[i])
    return result

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [42, 56, 14]
        self.assertEqual(solution(test), 14)

    def test_case_2(self):
        test = []
        self.assertRaises(RuntimeError, solution, test)

    def test_case_3(self):
        test = [2, 4, 6, 8, 16]
        self.assertEqual(solution(test), 2)

    def test_case_4(self):
        test = [9, 15, 22]
        self.assertEqual(solution(test), 1)

    def test_case_5(self):
        test = [22, 55]
        self.assertEqual(solution(test), 11)

if __name__ == '__main__':
    unittest.main()

