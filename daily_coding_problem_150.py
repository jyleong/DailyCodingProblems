'''
Given a list of points, a central point, and an integer k, 
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], 
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
'''

import heapq
import unittest
import math

def calc_dist(p1, p2):
    y_squared = (p2[1] - p1[1]) ** 2
    x_squared = (p2[0] - p1[0]) ** 2
    return math.sqrt(y_squared + x_squared)
    

def solution(points_list, center, k):
    if k > len(points_list):
        return points_list

    points_dist = dict()
    for point in points_list:
        dist = calc_dist(point, center)
        points_dist[point] = dist
    
    heap = []
    heapq.heapify(heap)

    tuples = [[val, key] for key,val in points_dist.items()]
    for i in range(len(tuples)):
        heapq.heappush(heap, tuples[i])

    # get k number of closest points

    nearest_points = []
    j = 0
    while j < k:
        point = heapq.heappop(heap)
        nearest_points.append(point[1])
        j += 1
    return nearest_points




class DailyCodingProblemsTest(unittest.TestCase):

    def test_case_1(self):
        points = [(0, 0), (5, 4), (3, 1)]
        center = (1, 2)
        k = 2
        result = [(0,0), (3, 1)]
        
        self.assertEqual(solution(points, center, k), result)

    def test_case_2(self):
        points = []
        center = (1, 2)
        k = 2
        result = []
        
        self.assertEqual(solution(points, center, k), result)

    def test_case_3(self):
        points = [(0, 0), (5, 4), (3, 1), (-1, -1)]
        center = (1, 2)
        k = 3
        result = [(0,0), (3, 1), (-1, -1)]
        
        self.assertEqual(solution(points, center, k), result)

if __name__ == '__main__':
    unittest.main()


