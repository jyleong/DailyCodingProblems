'''
This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
'''
import unittest

def most_coins(mat):
    if not mat or len(mat) == 0 or len(mat[0]) == 0:
        return 0
    DP = [row[:] for row in mat]
    for i in range(1, len(mat)):
        DP[i][0] += DP[i-1][0]
    for j in range(1, len(mat[0])):
        DP[0][j] += DP[0][j-1]

    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            DP[i][j] += max(DP[i][j-1], DP[i-1][j])
    return DP[len(mat)-1][len(mat[0])-1]
    


class Daily_Coding_Problem_Test(unittest.TestCase):

    def test_case_1(self):
        mat = []
        expected = 0
        self.assertEqual(most_coins(mat), expected)

    def test_case_2(self):
        mat = [[]]
        expected = 0
        self.assertEqual(most_coins(mat), expected)

    def test_case_3(self):
        mat = [[0, 3, 1, 1],
         [2, 0, 0, 4],
         [1, 5, 3, 1]]
        expected = 12
        self.assertEqual(most_coins(mat), expected)

    def test_case_4(self):
        mat = [[0, 3, 1, 1],[2, 6, 0, 4],[1, 5, 3, 1]]
        expected = 18
        self.assertEqual(most_coins(mat), expected)

    def test_Case_5(self):
        mat = [[0, 3, 1, 1],
         [2, 8, 9, 4],
         [1, 5, 3, 1]]
        expected = 25
        self.assertEqual(most_coins(mat), expected)
if __name__ == "__main__":

    unittest.main()

