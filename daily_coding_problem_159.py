'''
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
'''
import unittest

def solution(string):
    str_set = set()
    for c in string:
        if c not in str_set:
            str_set.add(c)
        else:
            return c
    return None

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = 'acbbac'
        self.assertEqual(solution(test), 'b')

    def test_case_2(self):

        test = 'acbdefg'
        self.assertEqual(solution(test), None)

    def test_case_3(self):
        test = ''
        self.assertEqual(solution(test), None)

if __name__ == '__main__':
    unittest.main()