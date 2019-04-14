'''
Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.

'''

import unittest

def count_mult(N, x):
    count = 0
    for i in range(1, N + 1):
        for j in range(i, N+1):
            if (i * j == x and i != j):
                count += 2
            elif (i * j == x and i == j):
                count += 1
    return count


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        N = 6
        x = 12
        
        expected = 4
        self.assertEqual(count_mult(N, x), expected)

    def test_case_2(self):
        N = 6
        x = 36
        
        expected = 1
        self.assertEqual(count_mult(N, x), expected)

    def test_case_3(self):
        N = 7
        x = 14
        
        expected = 2
        self.assertEqual(count_mult(N, x), expected)

    def test_case_4(self):

        N = 9
        x = 24
        
        expected = 4
        self.assertEqual(count_mult(N, x), expected)

if __name__ == '__main__':

    unittest.main()
