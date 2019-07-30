'''
Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
'''

import unittest

def matrix_range(matrix, i1, i2, j1, j2):
    result = 0
    height = len(matrix)
    width = len(matrix[0])
    if i1 < 0 or i1 >= height or i2 < 0 or i2 >= width \
    or j1 < 0 or j1 >= height or j2 < 0 or j2 >= width:
        return result

    # calc first point
    less_than = i1 * width + i2
    result += less_than
    more_than =  (height - j1 - 1) * width + (width - 1 - j2)
    result += more_than
    return result

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [[1, 3, 7, 10, 15, 20],
        [2, 6, 9, 14, 22, 25],
        [3, 8, 10, 15, 25, 30],
        [10, 11, 12, 23, 30, 35],
        [20, 25, 30, 35, 40, 45]]

        i1 = 1
        i2 = 1
        j1 = 3
        j2 = 3
        self.assertEqual(matrix_range(test, i1, i2, j1, j2), 15)

    def test_case_2(self):
        test = [[1, 3, 7, 10, 15, 20],
        [2, 6, 9, 14, 22, 25],
        [3, 8, 10, 15, 25, 30],
        [10, 11, 12, 23, 30, 35],
        [20, 25, 30, 35, 40, 45]]

        i1 = 1
        i2 = 3
        j1 = 4
        j2 = 4
        self.assertEqual(matrix_range(test, i1, i2, j1, j2), 10)




if __name__ == '__main__':

    unittest.main()
