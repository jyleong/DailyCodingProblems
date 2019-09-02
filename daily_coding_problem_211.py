'''
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

'''

import unittest

def pattern_occurences(target, pattern):
    if not target and not pattern \
            or len(pattern) > len(target):
        return []

    pattern_list = []
    pat = len(pattern)
    for i in range(0, len(target)-pat+1):
        if target[i:i+pat] == pattern:
            pattern_list.append(i)

    return pattern_list


class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = "abracadabra"
        pattern = "abr"
        result = [0, 7]
        self.assertEqual(pattern_occurences(test, pattern),result)

    def test_case_2(self):
        test = ''
        pattern = "abr"
        result = []
        self.assertEqual(pattern_occurences(test, pattern),result)

    def test_case_3(self):
        test = 'bbbbb'
        pattern = "bb"
        result = [0, 1, 2, 3]
        self.assertEqual(pattern_occurences(test, pattern),result)


if __name__ == '__main__':

    unittest.main()

