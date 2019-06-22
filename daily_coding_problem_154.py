'''
Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
'''

import unittest
import heapq

class StackApi(object):

    def __init__(self):
        self.heap_stack = []
        heapq.heapify(self.heap_stack)

    def peek(self):
        if not self.heap_stack:
            return None
        return self.heap_stack[0][1]

    def push(self, item):

        if not self.heap_stack:
            new_item = (0, item)    
        else:
            top_item = self.heap_stack[0]

            new_item = (top_item[0]-1, item)
        heapq.heappush(self.heap_stack, new_item)

    def pop(self):
        top_item = heapq.heappop(self.heap_stack)
        return top_item[1]

class DailyCodingProblemsTest(unittest.TestCase):

    def test_case_1(self):
        stack = StackApi()
        test_list = [5, 3, 2, 1, 0, 12, -1]
        self.assertEqual(stack.peek(), None)
        
        stack.push(test_list[0])
        stack.push(test_list[1])
        self.assertEqual(stack.peek(), 3)
        stack.push(test_list[2])

        self.assertEqual(stack.peek(), 2)

        stack.pop()
        self.assertEqual(stack.peek(), 3)
        stack.pop()
        stack.push(test_list[3])
        self.assertEqual(stack.peek(), 1)
        stack.push(test_list[4])
        stack.push(test_list[5])

        self.assertEqual(stack.peek(), 12)

        stack.pop()
        self.assertEqual(stack.peek(), 0)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.peek(), 5)
        stack.pop()
        self.assertEqual(stack.peek(), None)
        



if __name__ == '__main__':
    unittest.main()