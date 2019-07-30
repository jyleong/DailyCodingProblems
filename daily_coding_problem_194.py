'''
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

'''

import unittest

def num_intersect(p, q):
    if not p or not q:
        return 0

    pairs = []
    for i in range(len(p)):
        pairs.append((p[i], q[i]))
    count = 0
    for i in range(len(pairs)):
        for j in range(i):
            p1 = pairs[i]
            p2 = pairs[j]
            if p1[0] < p2[0] and p1[1] > p2[1] \
            or p2[0] < p1[0] and p2[1] > p1[1]:
                count += 1
    return count




class DailyCodingProblem(unittest.TestCase):

    def test_case_1(self):
        p = [1, 4, 5, 2]
        q = [2, -1, 6, 4]
        self.assertEqual(num_intersect(p, q), 2)

    def test_case_2(self):
        p = []
        q = []

        self.assertEqual(num_intersect(p, q), 0)

    def test_case_3(self):
        p = [1, 4, 5, 2]
        q = [1, 5, 5, 0]
        self.assertEqual(num_intersect(p, q), 1)

if __name__ == '__main__':

    unittest.main()
