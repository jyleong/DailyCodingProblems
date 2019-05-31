'''
This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.

'''


class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minValue(node):
    res = node
    while(res.left is not None):
        res = res.left
    return res

def inorder_successor(root, node):
    if (node.right is not None):
        return minValue(node.right)

    # else find from root traverse down

    current = root
    successor = None
    while(current is not None):
        
        if (current.val < node.val):
            # go right
            current = current.right
        elif (current.val > node.val):
            successor = current
            current = current.left
        else:
            break
    return successor

root = Node(20)
a = Node(8)
b = Node(35)
f = Node(22)
c = Node(12)
d = Node(14)
e = Node(4)
g = Node(10)
root.left = a
root.right = f
f.right = b
a.left = e
a.right = c
c.left = g
c.right = d

test_1 = inorder_successor(root, a)

print('8: ', test_1.val)

test_2 = inorder_successor(root, root)

print('20: ', test_2.val)

test_3 = inorder_successor(root, d)

print('14: ', test_3.val)

test_4 = inorder_successor(root, f)

print('22: ', test_4.val)








