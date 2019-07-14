'''
Given the sequence of keys visited by a postorder traversal of a binary search tree,
reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8
'''
'''
Taken inspiration from optmized solution of:
https://www.geeksforgeeks.org/construct-a-binary-search-tree-from-given-postorder/
'''
class BstNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

def build_bst(post_order_list):
    if not post_order_list:
        return None
    global_idx = [len(post_order_list) - 1]

    def construct_bst_util(arr, cur_node, min_val, max_val):
        if global_idx[0] < 0:
            return None
        node = None
        if cur_node > min_val and cur_node < max_val:

            # can create node
            node = BstNode(cur_node)
            global_idx[0] -= 1
            if global_idx[0] >= 0:
                node.right = construct_bst_util(arr, post_order_list[global_idx[0]], cur_node, max_val)
                node.left = construct_bst_util(arr, post_order_list[global_idx[0]], min_val, cur_node)

        return node

    return construct_bst_util(post_order_list, post_order_list[global_idx[0]], float('-inf'), float('inf'))

def print_inorder (node) :

    if (node == None) :
        return
    print_inorder(node.get_left())
    print(node.get_val(), end = " ")
    print_inorder(node.get_right())

if __name__ == '__main__':

    test = [2, 4, 3, 8, 7, 5]

    bst_tree = build_bst(test)

    print_inorder(bst_tree)

