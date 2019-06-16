'''
Given a 2-D matrix representing an image, a location of a pixel in the 
screen and a color C, replace the color of the given pixel and all adjacent 
same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
'''
import unittest

def solution(image, location, color):
    if location[1] > len(image) or location[0] > len(image[0]):
        return image
    color_at_loc = image[location[1]][location[0]]
    # flood fill algo
    pixel_queue = []
    pixel_queue.append(location)
    # this stack to always gold the color to replace
    # visited_set = set()
    while len(pixel_queue) > 0:
        p = pixel_queue.pop(0)
        x = p[0]
        y = p[1]
        # replace
        if image[y][x] == color_at_loc:
            image[y][x] = color
            # go U D L R
            
            if y-1 >= 0 and image[y-1][x] == color_at_loc:
                pixel_queue.append((x, y-1))
                #image[y-1][x] == color
            if y+1 < len(image) and image[y+1][x] == color_at_loc:
                pixel_queue.append((x, y+1))
                #image[y+1][x] == color
            if x-1 >= 0 and image[y][x-1] == color_at_loc:
                pixel_queue.append((x-1, y))
                #image[y][x-1] == color
            if x+1 < len(image[0]) and image[y][x+1] == color_at_loc:
                pixel_queue.append((x+1, y))
                #image[y][x+1] == color
    return image


class DailyCodingProblemsTest(unittest.TestCase):

    def test_case_1(self):
        image = [['B', 'B', 'W'], 
        ['W', 'W', 'W'], 
        ['W', 'W', 'W'], 
        ['B', 'B', 'B']]
        location = (2, 2)
        color = 'G'
        result = [['B', 'B', 'G'], 
        ['G', 'G', 'G'], 
        ['G', 'G', 'G'], 
        ['B', 'B', 'B']]
        
        self.assertEqual(solution(image, location, color), result)


if __name__ == '__main__':
    unittest.main()
