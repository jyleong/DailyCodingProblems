'''
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''

import heapq

min_heap = []
max_heap = []

stream_1 = [2,1,5,7,2,0,5]
def add_to_stream(number):
    heapq.heappush(min_heap, number)
    n = heapq.heappop(min_heap)
    heapq.heappush(max_heap, -n)
    if (len(min_heap) < len(max_heap)):
        nu = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -nu)

def get_median():
    size = len(min_heap) + len(max_heap)
    if (size % 2 == 1):
        return min_heap[0]
    else:
        return (min_heap[0] - max_heap[0])/2

for i in stream_1:
    add_to_stream(i)
    print("median at {}: {}".format(i, get_median()))
