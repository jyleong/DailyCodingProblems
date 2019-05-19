'''
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
'''
import unittest

def lcs(a, b):
    
    DP = [[0]*(len(a)+1) for _ in range(len(b)+1)] 

    for i in range(len(DP)):
        for j in range(len(DP[0])):
            if not i or not j:
                DP[i][j] = 0
            elif a[i-1] == b[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j])
    return DP[len(a)][len(a)]

def k_palindrome(str, k):
    rev = str[::-1]
    
    return (len(str) - lcs(str, rev)) <= k
    

class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        test = 'waterrfetawx'
        k = 2
        expected = True
        self.assertEqual(k_palindrome(test, k), expected)

    def test_case_2(self):
        test = ''
        k = 2
        expected = True
        self.assertEqual(k_palindrome(test, k), expected)

    def test_case_3(self):
        test = 'abca'
        k = 1
        expected = True
        self.assertEqual(k_palindrome(test, k), expected)

    def test_case_4(self):
        test = 'abc'
        k = 1
        expected = False
        self.assertEqual(k_palindrome(test, k), expected)

if __name__ == '__main__':

    unittest.main()
