'''
Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
'''

import unittest
from collections import defaultdict

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def freq_sum(node):
    if not node:
        return 0
    sums = defaultdict(int)

    def freq_sum_helper(root, sum_dict):
        if not root:
            return 0
        if not root.left and not root.right:
            sum_dict[root.val] += 1
            return root.val
        cur_sum = root.val + \
                freq_sum_helper(root.left, sum_dict) \
                + freq_sum_helper(root.right, sum_dict)
        sum_dict[cur_sum] += 1
        return cur_sum
    freq_sum_helper(node, sums)
    most_freq_sum = max(sums.items(), key=lambda val: val[1])[0]
    return most_freq_sum

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        n1 = Node(5)
        n2 = Node(2)
        n3 = Node(-5)
        n1.left = n2
        n1.right = n3
        self.assertEqual(freq_sum(n1), 2)

    def test_case_2(self):
        n1 = None
        self.assertEqual(freq_sum(n1), 0)

    def test_case_3(self):
        n1 = Node(2)
        n2 = Node(3)
        n3 = Node(1)
        n4 = Node(1)
        n5 = Node(1)
        n6 = Node(5)
        n7 = Node(3)
        n8 = Node(2)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6
        n3.right = n7
        n7.left = n8
        self.assertEqual(freq_sum(n1), 5)




if __name__ == '__main__':
    unittest.main()

