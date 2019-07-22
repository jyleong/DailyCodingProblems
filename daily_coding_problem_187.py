'''
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
'''
import unittest

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(object):
    def __init__(self, rect_coords):
        self.tl = Point(rect_coords['top_left'][0],rect_coords['top_left'][1])
        dim = rect_coords['dimensions']
        self.br = Point(rect_coords['top_left'][0] + dim[0],\
                rect_coords['top_left'][1] - dim[1])

    def envelopes(self, rect):
        return self.tl.x <= rect.tl.x and self.tl.y >= rect.tl.y \
        and self.br.x >= rect.br.x and self.br.y <= rect.br.y

def check_any_overlap(rect_list):
    if not rect_list or len(rect_list) <= 1:
        return False

    for i in range(0, len(rect_list)):
        for j in range(i+1, len(rect_list)):
            rect_1 = rect_list[i]
            rect_2 = rect_list[j]
            if rect_1.envelopes(rect_2) or rect_2.envelopes(rect_1):
                return True
    return False

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
        r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
        r3 = Rectangle({"top_left": (0, 5), "dimensions": (4, 4)})
        test = [r1, r2, r3]
        self.assertTrue(check_any_overlap(test))

    def test_case_2(self):
        r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
        r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
        r3 = Rectangle({"top_left": (2, 5), "dimensions": (4, 4)})
        test = [r1, r2, r3]
        self.assertFalse(check_any_overlap(test))

    def test_case_3(self):
        r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
        r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
        test = [r1, r2]
        self.assertFalse(check_any_overlap(test))

    def test_case_4(self):
        self.assertFalse(check_any_overlap([]))

if __name__ == '__main__':

    unittest.main()


