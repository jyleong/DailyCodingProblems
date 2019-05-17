'''
Given a set of closed intervals, find the smallest set of numbers 
that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], 
one set of numbers that covers all these intervals is {3, 6}.
'''
import sys

def covers_intervals(intervals):
    if (intervals is None or len(intervals) == 0):
        return []
    intervals.sort(key=lambda e: e[1])

    result = []
    result.append(intervals[0][1])
    cur = intervals[0]
    for i in range(1, len(intervals)):
        if (intervals[i][0] > cur[1]):
            if (intervals[i][1] < cur[1]): # should replace?
                result.pop(-1)
            cur = intervals[i]
            result.append(intervals[i][1])

    return result



    


assert covers_intervals([[0, 3]]) == [3]
assert covers_intervals([[0, 3], [2, 6]]) == [3]
assert covers_intervals([[0, 3], [2, 6], [3, 4]]) == [3]
assert covers_intervals([[0, 3], [2, 6], [3, 4], [6, 7]]) == [3, 7]
assert covers_intervals([[0, 3], [2, 6], [3, 4], [6, 9]]) == [3, 9]
assert covers_intervals([[0, 3], [2, 6], [3, 4], [6, 100]]) == [3, 100]

assert covers_intervals([[0, 4], [1, 2], [5, 7], [6, 7], [6, 9], [8, 10]]) == [2, 7, 10]
