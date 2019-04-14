'''
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, 
multiplication, or modulus operators. Return the quotient as an integer, 
ignoring the remainder.
'''
import unittest

def divide(dividend, divisor):
    if (dividend == 0):
        return 0
    if (divisor == 0):
        raise Exception('Cannot divide by zero')
    quotient = 0
    while(dividend >= divisor):
        dividend -= divisor
        quotient += 1
    return quotient


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        dividend = 50
        divisor = 5
        expected = 10
        self.assertEqual(divide(dividend, divisor), expected)

    def test_case_2(self):
        dividend = 24
        divisor = 3
        expected = 8
        self.assertEqual(divide(dividend, divisor), expected)

    def test_case_3(self):
        dividend = 25
        divisor = 3
        expected = 8
        self.assertEqual(divide(dividend, divisor), expected)

    def test_case_4(self):
        dividend = 5
        divisor = 8
        expected = 0
        self.assertEqual(divide(dividend, divisor), expected)

    def test_case_5(self):
        dividend = 79
        divisor = 7
        expected = 11
        self.assertEqual(divide(dividend, divisor), expected)

    def test_case_5(self):
        dividend = 50
        divisor = 0

        with self.assertRaises(Exception) as context:
            divide(dividend, divisor)

        self.assertTrue('Cannot divide by zero' in str(context.exception))

if __name__ == '__main__':

    unittest.main()

