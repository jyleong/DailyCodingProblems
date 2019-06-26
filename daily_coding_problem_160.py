'''
This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.
'''


def get_max_weight():
    
    nodes = dict()
    nodes['a'] = [('b', 3), ('c', 5), ('d', 8)]
    nodes['b'] = [('a', 3)]
    nodes['c'] = [('a', 5)]
    nodes['d'] = [('a', 8), ('e', 2), ('f', 4)]
    nodes['e'] = [('d', 2), ('g', 1), ('h', 1)]
    nodes['f'] = [('d', 4)]
    nodes['g'] = [('e', 1)]
    nodes['h'] = [('e', 1)]

    cur_max = 0
    path_max = None
    for k, v in nodes.items():
        node_max, path = max_weight_helper(k, nodes, set())
        if node_max > cur_max:
            cur_max = node_max
            path_max = path
        
    return cur_max, path_max

def max_weight_helper(cur_node, nodes, visited_set):
    max_sum = 0
    cur_path = [cur_node]
    visited_set.add(cur_node)
    for tup in nodes[cur_node]:
        if tup[0] not in visited_set:
            
            cur_weight, path = max_weight_helper(tup[0], nodes, visited_set)
            val = tup[1] + cur_weight
            if val > max_sum:
                max_sum = val
                cur_path = [cur_node] + path
            
    visited_set.remove(cur_node)
    return max_sum, cur_path

if __name__ == '__main__':
    max_weight, path_max = get_max_weight()
    print('max weight of graph: ', max_weight)
    print('max path: ', path_max)
    assert max_weight == 17


