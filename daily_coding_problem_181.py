'''
Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
'''

import unittest

def is_pali(s):
    l = len(s)
    i = 0
    while i < l//2+1:
        if s[i] != s[l-1-i]:
            return False
        i += 1
    return True

def solution(string):
    dp = dict()
    def dfs(s, left, right):
        if len(s[left:right]) == 1 or is_pali(s[left:right]):
            dp[s[left:right]] = [s[left:right]]
            return dp[s[left:right]]
        else:
            cuts = float('inf')
            cur_answer = []

            for i in range(left+ 1, right):
                left_soln = []
                right_soln = []
                left_part = s[0:i]
                right_part = s[i: right]
                if left_part in dp:
                    left_soln = dp[left_part]
                else:
                    left_soln = dfs(s, 0, i)
                    dp[left_part] = left_soln
                if right_part in dp:
                    right_soln = dp[right_part]
                else:
                    right_soln = dfs(s, i, right)
                    dp[right_part] = right_soln
                if 1 + len(right_soln) + len(left_soln) < cuts:
                    cuts = 1 + len(right_soln) + len(left_soln)
                    cur_answer = right_soln + left_soln
            return cur_answer
    return dfs(string, 0, len(string))

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = 'racecarannakayak'
        result = ["kayak", "anna", "racecar"]
        self.assertEqual(solution(test), result)

    def test_case_2(self):
        test = 'abc'
        result = ['c', 'b', 'a']
        self.assertEqual(solution(test), result)

if __name__ == '__main__':
    unittest.main()


