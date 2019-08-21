'''Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".'''

import unittest

def min_parenthesis(input):
    if not input:
        return input
    count = 0
    result = ""
    for p in input:
        if p == '(':
            result += p
            count += 1
        if p == ')' and count > 0:
            result += p
            count -= 1
    if count > 0:
        result += ')' * count
    return result

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = '(()'
        result = '(())'
        self.assertEqual(min_parenthesis(test), result)

    def test_case_2(self):
        test = '))()('
        result = '()()'
        self.assertEqual(min_parenthesis(test), result)


if __name__ == '__main__':

    unittest.main()


