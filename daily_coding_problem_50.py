'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
'''

class node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def evalTree(root):
    if (root.left is None and root.right is None):
        return int(root.data)

    left_val = evalTree(root.left)
    right_val = evalTree(root.right)

    # check which operation to apply 
    if root.data == '+': 
        return left_val + right_val 
      
    elif root.data == '-': 
        return left_val - right_val 
      
    elif root.data == '*': 
        return left_val * right_val 
      
    else: 
        return left_val / right_val

# Driver function to test above problem 
if __name__=='__main__': 
      
    # creating a sample tree 
    root = node('+') 
    root.left = node('*') 
    root.left.left = node('5') 
    root.left.right = node('4') 
    root.right = node('-') 
    root.right.left = node('100') 
    root.right.right = node('20') 
    print(evalTree(root))
  
    root = None
  
    #creating a sample tree 
    root = node('+') 
    root.left = node('*') 
    root.left.left = node('5') 
    root.left.right = node('4') 
    root.right = node('-') 
    root.right.left = node('100') 
    root.right.right = node('/') 
    root.right.right.left = node('20') 
    root.right.right.right = node('2') 
    print(evalTree(root))
