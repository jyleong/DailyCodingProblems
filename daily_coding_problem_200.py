'''
Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X contains at least one point in P. Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
'''

import unittest

def stab_intervals(intervals):
    result = []
    if not intervals or len(intervals) == 0:
        return result

    curr = intervals[0]
    for i in range(1,len(intervals)):
        if intervals[i][0] > curr[1]:
            result.append(curr[1])
            curr = intervals[i]

    if result[-1] < intervals[i][0]:
        result.append(intervals[i][0])
    return result

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = [(1, 4), (4, 5), (7, 9), (9, 12)]
        result = [4, 9]
        self.assertEqual(stab_intervals(test), result)

    def test_case_2(self):

        test = [(1, 2), (4, 5), (7, 9), (9, 12)]
        result = [2, 5, 9]
        self.assertEqual(stab_intervals(test), result)

    def test_case_3(self):

        test = [(1, 4), (4, 7), (6, 8), (9, 12)]
        result = [4, 8, 9]
        self.assertEqual(stab_intervals(test), result)


if __name__ == '__main__':

    unittest.main()
