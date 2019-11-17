'''
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
'''

import unittest

def shortest_standard_path(abs_path):
    if not abs_path or len(abs_path) == 0:
        raise Exception('Invalid input')
    dirs = abs_path.split('/')
    if dirs[0] == '..':
        raise Exception('No further higher directory')
    paths_arr = []

    for d in dirs:
        if d == '.':
            continue
        elif d == '..':
            paths_arr.pop()
        else:
            paths.append(d)

    return '/'.join(paths_arr)


class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = './'
        result = '/'
        self.assertEquals(shortest_standard_path(test), result)

    def test_case_2(self):
        test = "/usr/bin/../bin/./scripts/../"
        result = '/usr/bin/'
        self.assertEquals(shortest_standard_path(test), result)

    def test_case_2(self):
        test = "/../"
        
        self.assertRaises(Exception, shortest_standard_path, test)
