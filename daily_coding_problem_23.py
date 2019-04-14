import unittest
'''

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum 
number of steps required to reach the end coordinate from the start. If there is 
no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number 
of steps required to reach the end is 7, since we would need to go through (1, 2) 
because there is a wall everywhere else on the second row.
'''
# do L U R D
ROW_ARR = [0, -1, 0, 1]
COL_ARR = [-1, 0, 1, 0]

class Position(object):
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

def is_valid(r, c, r_len, c_len):
    return (r >= 0 and c >= 0) and (r < r_len and c < c_len)


'''
input: matrix[M][N], start tuple coordinates, end tuple corrdinates
output: integer that is least possible moves to get to destination
or else return -1 to represent invalid
'''
def numMoves(matrix, start, end):
    if (matrix[start[0]][start[1]] or matrix[end[0]][end[1]]):
        print("Invalid start or end parameters")
        return -1

    r_len = len(matrix)
    c_len = len(matrix[0])
    # rowVisited = [False] * len(matrix)
    # print(rowVisited)
    # visitedMatrix = []
    # for i in range(len(matrix[0])):
    #     visitedMatrix.append(rowVisited)
    
    queueMoves = []
    position = Position(start[0], start[1], 0)
    queueMoves.append(position)
    # marks start visited true
    # visitedMatrix[start[0]][start[1]] = True
    # print(visitedMatrix)
    
    while(len(queueMoves) != 0):
        posi = queueMoves[0]
        
        # if we have reach end return  distance
        if (posi.x == end[0] and posi.y == end[1]):
            return posi.dist

        # nevermind, move on, remove from front, put all its valid neighbours into queue
        queueMoves = queueMoves[1:]

        for idx in range(4):
            # print("Iteration {}: ({}, {})".format(idx, posi.x, posi.y))
            # print("Iteration {}: (candidate Row {}, candidate Col{})".format(idx, posi.x + ROW_ARR[idx], COL_ARR[idx]))
            row = posi.x + ROW_ARR[idx]
            col = posi.y + COL_ARR[idx]
            
            if (is_valid(row, col, r_len, c_len) and \
                not matrix[row][col]):

                new_position = Position(row, col, posi.dist + 1)
                # print("new position!!!!!!!!!!!")
                # print("({}, {})".format(new_position.x, new_position.y))
                # print("!!!!!!!!!!!!!!!new position!]")
                
                queueMoves.append(new_position)
                # mark visited
                matrix[row][col] = True

    return -1
    # error if not reached




class Binary_Matrix_Test(unittest.TestCase):
    def test_case_1(self):
        test_case = [[False, False, False, False],
                    [True, True, False, True],
                    [False, False, False, False],
                    [False, False, False, False]]
        start = (3 ,0)
        end = (0,0)
        self.assertEqual(numMoves(test_case, start, end), 7)

    def test_case_2(self):

        test_case = [[False, False, False, False, True],
                    [True, False, False, True, False],
                    [True, True, False, False, False],
                    [False, False, False, False, True],
                    [False, True, False, False, True],
                    [True, True, False, False, True]]
        start = (0 ,1)
        end = (5, 3)
        self.assertEqual(numMoves(test_case, start, end), 7)





if __name__ == '__main__':

    unittest.main()

