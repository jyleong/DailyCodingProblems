'''
You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
'''

import unittest

def correct_order_letters(sorted_words):
    char_graph = dict()
    # setup the adjacency list / graph
    for w in sorted_words:
        for c in w:
            if c not in char_graph:
                char_graph[c] = set()
    for i in range(len(sorted_words)-1):
        w1 = sorted_words[i]
        w2 = sorted_words[i+1]
        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            if w1[j] != w2[j]:
                char_graph[w1[j]].add(w2[j])
                break
    # Sort through graph and output to lexical_order
    visited_set = set()
    lexical_stack = []

    def topological_sort(graph, cur, visited, lexical_stack):
        visited.add(cur)
        for neighbour in graph[cur]:
            if neighbour not in visited:
                topological_sort(graph,
                        neighbour, visited, lexical_stack)
        lexical_stack.append(cur)

    for c in char_graph.keys():
        if c not in visited_set:
            topological_sort(char_graph,
                    c, visited_set, lexical_stack)

    return lexical_stack[::-1]

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        sorted_words = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']

        actual = ['x', 'z', 'w', 'y']
        expected = correct_order_letters(sorted_words)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        sorted_words = ['baa', 'abcd', 'abca', 'cab', 'cad']

        actual = ['b', 'd', 'a', 'c']
        expected = correct_order_letters(sorted_words)
        self.assertEqual(actual, expected)

if __name__ == '__main__':

    unittest.main()



