'''
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
'''

import unittest

def max_triangle_path(triangle):
    def path_helper(triangle, level, index, cur_path, cur_sum):
        if level == len(triangle) - 1:
            return cur_path, cur_sum

        left_path, left_sum  = path_helper(triangle, level + 1, index, \
                cur_path + [triangle[level + 1][index]], cur_sum + triangle[level + 1][index])
        right_path, right_sum  = path_helper(triangle, level + 1, index + 1, \
                cur_path + [triangle[level + 1][index + 1]], cur_sum + triangle[level + 1][index + 1])
        if left_sum > right_sum:
            return left_path, left_sum
        else:
            return right_path, right_sum
    max_path, max_sum = path_helper(triangle, 0, 0, [triangle[0][0]], triangle[0][0])
    return max_path

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [[1], [2, 3], [1, 5, 1]]
        result = [1, 3, 5]
        self.assertEqual(max_triangle_path(test), result)

    def test_case_2(self):
        test = [[1], [3, 5], [7, 4, 3]]
        result= [1, 3, 7]
        self.assertEqual(max_triangle_path(test), result)


if __name__ == '__main__':

    unittest.main()


