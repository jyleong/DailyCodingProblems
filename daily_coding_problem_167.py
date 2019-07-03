'''
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
'''

import unittest

def is_pali(word):

    i = 0
    e = len(word)-1
    while i < e:
        if word[i] != word[e]:
            return False
        i += 1
        e -= 1
    return True

def palindrome_pairs(arr):
    if not arr or len(arr) <= 1:
        return []
    result = []

    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if is_pali(arr[i] + arr[j]):
                result.append((i, j))
            if is_pali(arr[j]+ arr[i]):
                result.append((j, i))
    return result

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = ["code", "edoc", "da", "d"]
        result = [(0, 1), (1, 0), (2, 3)]
        self.assertEqual(palindrome_pairs(test), result)

    def test_case_2(self):
        test = ["code", "edoc", "da", "d", "coded", "oc"]
        result = [(0, 1), (1, 0), (4, 1), (2, 3), (4, 5)]
        self.assertEqual(palindrome_pairs(test), result)

    def test_case_3(self):
        test = []
        result = []
        self.assertEqual(palindrome_pairs(test), result)

    def test_case_4(self):
        test = ["codedoc"]
        result = []
        self.assertEqual(palindrome_pairs(test), result)




if __name__ == '__main__':
    unittest.main()