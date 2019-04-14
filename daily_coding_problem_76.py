'''
This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns 
that can be removed to ensure that each row is ordered from top to bottom lexicographically. 
That is, the letter at each column is lexicographically later as you go down each row. It does 
not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.

'''

import unittest

def count_lex(arr):
    count = 0
    if (len(arr) <= 1):
        return count
    row = len(arr)
    col = len(arr[0])
    for i in range(col):
        for j in range(1, row):
            if arr[j][i] < arr[j-1][i]:
                count += 1
                break
    return count


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        arr = ['cba', 'daf', 'ghi']
        
        expected = 1
        self.assertEqual(count_lex(arr), expected)

    def test_case_2(self):
        arr = ['abcdef']
        
        expected = 0
        self.assertEqual(count_lex(arr), expected)

    def test_case_3(self):
        arr = ['zyx', 'wvu', 'tsr']
        
        expected = 3
        self.assertEqual(count_lex(arr), expected)

if __name__ == '__main__':

    unittest.main()
