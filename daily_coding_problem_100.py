'''
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''
import unittest
import math

def count_steps(points):
    steps = 0;
    if not points or len(points) == 0:
        return steps
    for i in range(1, len(points)):
        dist = max(abs(points[i][1] - points[i-1][1]), abs(points[i][0] - points[i-1][0]))
        steps += dist
    return steps


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        points = [(0, 0), (1, 1), (1, 2)]
        expected = 2
        self.assertEqual(count_steps(points), expected)

    def test_case_2(self):
        points = [(0, 0), (1, 2), (4, 4)]
        expected = 5
        self.assertEqual(count_steps(points), expected)

    def test_case_3(self):
        points = []
        expected = 0
        self.assertEqual(count_steps(points), expected)

if __name__ == '__main__':

    unittest.main()