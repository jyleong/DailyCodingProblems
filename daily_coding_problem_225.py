'''
This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
'''

import unittest

def prisoners_circle(N, k):
    arr = list(range(1, N+1))
    survivor = None
    idx = 0
    while arr:
        idx = (idx + k - 1) % len(arr)
        # remove prisoner
        survivor = arr[idx]
        arr = arr[:idx] + arr[idx + 1:]
    return survivor

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        N = 5
        k = 2
        expected = 3
        self.assertEquals(prisoners_circle(N, k), expected)

    def test_case_2(self):
        N = 3
        k = 2
        expected = 3
        self.assertEquals(prisoners_circle(N, k), expected)

    def test_case_3(self):
        N = 5
        k = 3
        expected = 4
        self.assertEquals(prisoners_circle(N, k), expected)

if __name__ == '__main__':

    unittest.main()

