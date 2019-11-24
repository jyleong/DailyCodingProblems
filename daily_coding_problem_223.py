'''
Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, where h is the height of the tree. Write a program to compute the in-order traversal of a binary tree using O(1) space.

'''

class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node: %s left val: %s right val: " % (self.value, self.left, self.right)

def morris_inorder_traversal(root):
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.value)
            current = current.right
        else:
            # has left, get predecessor
            predecessor = find_predecessor(current)

            # assign predecssor right to current node
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                # when we are visiting most right and has child
                # break connection and go right
                predecessor.right = None
                result.append(current.value)
                current = current.right

    return result

def find_predecessor(node):
    current = node.left
    while current.right and current.right != node:
        current = current.right
    return current

def inorder_traversal(root):
    result = []

    def inorder_recurse(node, arr=[]):
        if node.left:
            inorder_recurse(node.left, arr)

        arr.append(node.value)

        if node.right:
            inorder_recurse(node.right, arr)
    inorder_recurse(root, result)
    return result

if __name__ == '__main__':

    root = Node(10)
    five = Node(5)
    thirty = Node(30)
    neg_two = Node(-2)
    six = Node(6)
    eight = Node(8)
    two = Node(2)
    neg_one = Node(-1)
    forty = Node(40)

    root.left = five
    root.right = thirty
    thirty.right = forty

    five.left = neg_two
    five.right = six
    six.right = eight

    neg_two.right = two
    two.left = neg_one

    expected = [-2, -1, 2, 5, 6, 8, 10, 30, 40]
    actual = morris_inorder_traversal(root)
    regular_inorder = inorder_traversal(root)
    assert actual == expected
    assert actual == regular_inorder
