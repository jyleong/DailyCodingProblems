'''
A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.

'''

import unittest

def check_min_connected(graph):
    visited_set = set()
    queue = []
    for k, v in graph.items():
        queue.append(k)
        break
    while len(queue) > 0:
        g = queue.pop(0)
        if g not in visited_set:
            visited_set.add(g)
        else:
            return False
        for gn in graph[g]:
            queue.append(gn)
    return True

class DailyCodingProblem(unittest.TestCase):

    def test_case_1(self):
        test = {'a': ['b', 'c'],
                'b': ['d'],
                'c': [],
                'd': []}
        self.assertTrue(check_min_connected(test))

    def test_case_2(self):
        test = {'a': ['b'],
                'b': ['d'],
                'd': []}
        self.assertTrue(check_min_connected(test))

    def test_case_3(self):
        test = {'a': ['b', 'c'],
                'b': ['d'],
                'c': ['b'],
                'd': ['a']}
        self.assertFalse(check_min_connected(test))


if __name__ == '__main__':

    unittest.main()
