'''
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, 
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
'''

import unittest

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else: # op == '/'
        return a / b

EXPRESSION_SET = set(['+', '/', '*', '-'])

def eval_expression(arr):
    operand_stack = []
    for item in arr:
        if item in EXPRESSION_SET:
            op_2 = operand_stack.pop()
            op_1 = operand_stack.pop()

            result = calculate(op_1, op_2, item)

            operand_stack.append(result)
        else:
            operand_stack.append(item)
    return operand_stack[0]

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [5, 3, '+']
        result = 8
        self.assertEqual(eval_expression(test), result)

    def test_case_2(self):
        test = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
        result = 5
        self.assertEqual(eval_expression(test), result)

if __name__ == '__main__':

    unittest.main()