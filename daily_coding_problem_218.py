'''
Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
'''

import unittest

def reverse_graph(graph):

    reversed_graph = {}
    for k, v in graph.items():
        reversed_graph[k] = []

    for node, connections in graph.items():
        for c in connections:
            reversed_graph[c].append(node)
    return reversed_graph

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = {'A': ['B', 'C'],
                'B': ['D'],
                'C': [],
                'D': []}
        expected = {'A': [],
                    'B': ['A'],
                    'C': ['A'],
                    'D': ['B']}
        actual = reverse_graph(test)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        test = {'A': ['B'],
                'B': ['C'],
                'C': []}
        expected = {'A': [],
                    'B': ['A'],
                    'C': ['B']}
        actual = reverse_graph(test)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        test = {'A': ['C'],
                'B': ['C'],
                'C': []}
        expected = {'A': [],
                    'B': [],
                    'C': ['A', 'B']}
        actual = reverse_graph(test)
        self.assertEqual(actual, expected)


if __name__ == '__main__':

    unittest.main()
