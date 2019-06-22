'''
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, 
since there's no rearrangement that can form a palindrome.
'''

import unittest

def solution(string):
    char_count = dict()

    # even length count must be even charcount += %2

    for c in string:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    final_count = 0
    for key in char_count:
        final_count += char_count[key] % 2
    return final_count <= 1


class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = 'carrace'
        self.assertEqual(solution(test), True)

    def test_case_2(self):
        test = ''
        self.assertEqual(solution(test), True)

    def test_case_3(self):
        test = 'daily'
        self.assertEqual(solution(test), False)

if __name__ == '__main__':
    unittest.main()