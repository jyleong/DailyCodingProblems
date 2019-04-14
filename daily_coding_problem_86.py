'''
Given a string of parentheses, write a function to compute the minimum number of 
parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", 
you should return 2, since we must remove all of them.
'''

import unittest

LEFT_PAREN = '('
RIGHT_PAREN = ')'
def min_removals(str):
    count = 0
    if (str is None or str == ""):
        return count
    stack = []
    for i in range(len(str)):
        if LEFT_PAREN == str[i]:
            stack.append(LEFT_PAREN)
        else:
            if len(stack) > 0 and stack[-1] == LEFT_PAREN:
                stack.pop()
            else:
                count += 1
    count += len(stack)
    return count


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        test = "()())()"
        expected = 1
        self.assertEqual(min_removals(test), expected)

    def test_case_2(self):
        test = ")("
        expected = 2
        self.assertEqual(min_removals(test), expected)

    def test_case_3(self):
        test = ")))()"
        expected = 3
        self.assertEqual(min_removals(test), expected)

    def test_case_4(self):
        test = ""
        expected = 0
        self.assertEqual(min_removals(test), expected)

    def test_case_5(self):
        test = "()((("
        expected = 3
        self.assertEqual(min_removals(test), expected)

    def test_case_5(self):
        test = ")()((("
        expected = 4
        self.assertEqual(min_removals(test), expected)

if __name__ == '__main__':

    unittest.main()