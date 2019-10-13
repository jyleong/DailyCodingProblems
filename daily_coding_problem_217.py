'''This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.'''

import unittest

def smallest_sparse(num):
    repeat_one = False
    prev_digit = 0
    temp = num
    length = 0
    while temp > 0:
        last_digit = temp & 1
        if last_digit == 1 and prev_digit == 1:
            repeat_one = True
        prev_digit = last_digit
        temp >>= 1
        length += 1
    if not repeat_one:
        return num
    else:
        new_num = 2 ** length
    return new_num

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = 22
        expected = 32
        actual = smallest_sparse(test)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        test = 21
        expected = 21
        actual = smallest_sparse(test)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        test = 3
        expected = 4
        actual = smallest_sparse(test)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        test = 255
        expected = 256
        actual = smallest_sparse(test)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        test = 0
        expected = 0
        actual = smallest_sparse(test)
        self.assertEqual(actual, expected)


if __name__ == '__main__':

    unittest.main()


