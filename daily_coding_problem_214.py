import unittest
'''
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''

def consecutive_ones(number):

    if number == 0:
        return 0
    max_ones = 0
    cur_ones = 0
    runs = False
    while number != 0:
        if number & 1 == 1:
            if not runs:
                runs = not runs
            cur_ones += 1
        else:
            if runs:
                runs = not runs
            max_ones = max(max_ones, cur_ones)
            cur_ones = 0

        number >>=1
    max_ones = max(max_ones, cur_ones)
    return max_ones


class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = 170
        expected = 1
        actual = consecutive_ones(test)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        test = 12
        expected = 2
        actual = consecutive_ones(test)
        self.assertEqual(actual, expected)

    def test_case_3(self):

        test = 255
        expected = 8
        actual = consecutive_ones(test)
        self.assertEqual(actual, expected)

    def test_case_4(self):

        test = 1279
        expected = 8
        actual = consecutive_ones(test)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        test = 156
        expected = 3
        actual = consecutive_ones(test)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
