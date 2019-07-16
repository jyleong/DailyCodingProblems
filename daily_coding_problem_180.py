import unittest
from collections import deque

def interleave(stack):
    queue = deque([]);
    length= len(stack)

    for i in range(length):
        queue.append(stack.pop())

    for i in range(length):
        if i < length//2:
           queue.append(queue.popleft())
        else:
        # at this point stack will have more elem than queue if odd
           stack.append(queue.popleft())

    # interleaving portion
    for i in range(length):
        if i % 2 == 0:
            queue.append(stack.pop())
        else:
            queue.append(queue.popleft())


    for i in range(length):
        stack.append(queue.popleft())
    return stack



class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):

        test = [1, 2, 3, 4, 5]
        result = [1, 5, 2, 4, 3]
        self.assertEqual(interleave(test), result)

    def test_case_2(self):

        test = [1, 2, 3, 4]
        result = [1, 4, 2, 3]
        self.assertEqual(interleave(test), result)

    def test_case_3(self):

        test = []
        result = []
        self.assertEqual(interleave(test), result)


if __name__ == '__main__':
    unittest.main()
