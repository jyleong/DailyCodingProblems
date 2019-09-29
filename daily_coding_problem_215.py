'''
The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
'''

from collections import defaultdict

class BinaryNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def assign_left(self, val):
        self.left = BinaryNode(val)
        return self.left

    def assign_right(self, val):
        self.right = BinaryNode(val)
        return self.right

def get_bottom_view(binary_node):
    horizontal_dist_dict = defaultdict(int)

    def get_horizontal_dist(binary_node, dist_dict, dist=0):

        dist_dict[dist] = binary_node.val
        if binary_node.left:
            get_horizontal_dist(binary_node.left, dist_dict, dist-1)
        if binary_node.right:
            get_horizontal_dist(binary_node.right, dist_dict, dist+1)


    get_horizontal_dist(binary_node, horizontal_dist_dict)
    # flatten and return values in dict sorted ascending
    sorted_dict = sorted(horizontal_dist_dict.items(), key=lambda x: x[0])
    return [x[1] for x in sorted_dict]

if __name__ == '__main__':
    five = BinaryNode(5)
    three = five.assign_left(3)
    seven = five.assign_right(7)
    one = three.assign_left(1)
    three.assign_right(4)
    one.assign_left(0)
    seven.assign_left(6)
    nine = seven.assign_right(9)
    nine.assign_left(8)

    expected = [0, 1, 3, 6, 8, 9]
    actual = get_bottom_view(five)
    assert actual == expected



