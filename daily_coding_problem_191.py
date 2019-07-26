'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
'''

import unittest

def min_itvl_remove(intervals):
    if not intervals or len(intervals) <= 1:
        return 0
    intervals.sort(key=lambda tup: tup[1])
    min_count = 0
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        ref_itvl = result[-1]
        cur_itvl = intervals[i]
        if cur_itvl[0] >= ref_itvl[0] and cur_itvl[0] < ref_itvl[1]:
            # must remove
            min_count += 1
        else:
            result.append(cur_itvl)
    return min_count

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [(7, 9), (2, 4), (5, 8)]
        result = 1
        self.assertEqual(min_itvl_remove(test), result)

    def test_case_2(self):
        test = []
        result = 0
        self.assertEqual(min_itvl_remove(test), result)

    def test_case_3(self):
        test = [(7, 9), (2, 4)]
        result = 0
        self.assertEqual(min_itvl_remove(test), result)

    def test_case_4(self):
        test = [(1, 4), (0, 3), (5, 9), (3, 7), (8, 10), (11, 12)]
        result = 2
        self.assertEqual(min_itvl_remove(test), result)



if __name__ == '__main__':
    unittest.main()
