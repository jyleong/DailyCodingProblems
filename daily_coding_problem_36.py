'''
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
'''

class Node(object):
    # Constructor to create a new node  
    def __init__(self, data):  
        self.key = data  
        self.left = None
        self.right = None

# A utility function to insert a new 
# node with given key in BST  
def insert(node, key): 
      
    # If the tree is empty, return a new node  
    if node == None: 
        return Node(key)  
  
    # Otherwise, recur down the tree  
    if key < node.key:  
        node.left = insert(node.left, key)  
    elif key > node.key:  
        node.right = insert(node.right, key)  
  
    # return the (unchanged) node pointer  
    return node 

def get_largest(node):
    current = node
    while(current.right):
        current = current.right
    return current.key

def second_largest(node):
    if not node:
        print("Error, node can't be none")
        return
    current = node
    while(current):
        if (current.left and not current.right):
            return get_largest(node.left)
        if (current.right
            and not current.right.left
            and not current.right.right):
            return current.key
        current = current.right


# Driver Code 
if __name__ == '__main__': 
      
    # Let us create following BST  
    #        50  
    #    /   \  
    #    30  70  
    #    / \ / \  
    # 20 40 60 80  
    root = None
    root = insert(root, 50)  
    insert(root, 30) 
    insert(root, 20)  
    insert(root, 40)  
    insert(root, 70)  
    insert(root, 60)  
    insert(root, 80)  
  
    print("test 1 should be 70 ", second_largest(root))

    root_2 = None
    root_2 = insert(root_2, 30)  
    insert(root_2, 20) 
    insert(root_2, 40)  
    insert(root_2, 45)  
    insert(root_2, 15)  
    insert(root_2, 28)  
    insert(root_2, 31)  

    print("test 2 should be 40 ", second_largest(root_2))

    root_3 = None
    root_3 = insert(root_3, 30)  
    insert(root_3, 20) 
    insert(root_3, 25)  

    print("test 3 should be 25 ", second_largest(root_3))