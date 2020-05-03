'''
You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be 5.
'''

import unittest

# n is number of eggs, k is number of floors
def solution(n, k):
    low = 1
    high = k
    while low < high:
        mid = low + (high-low)//2
        if get_bin_coefficient(mid, n) < k:
            low = mid + 1
        else:
            high = mid
    return low

# x is number of trials
def get_bin_coefficient(x, n):
    sum = 0
    cur_bin = 1
    for i in range(1, n+1):
        cur_bin *= x - i + 1
        cur_bin /= i
        sum += cur_bin
    return sum

class DailyCodingProblemTest(unittest.TestCase):

    def test_1(self):
        result = solution(2, 10)
        self.assertEqual(result, 4)

    def test_2(self):
        result = solution(1, 5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
