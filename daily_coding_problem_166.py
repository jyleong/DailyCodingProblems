'''
Implement a 2D iterator class. It will be initialized with an array of arrays, 
and should implement the following methods:

next(): returns the next element in the array of arrays. 
If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() 
repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
'''

class Iterator2D(object):

    def __init__(self, arr_2d):
        self.arr_2d = arr_2d
        self.generator = self.generate_2d()
        self.next_num = next(self.generator)

    def generate_2d(self):
        for arr in self.arr_2d:
            for val in arr:
                yield val

    def next(self):
        current = self.next_num
        try:
            self.next_num = next(self.generator)
        except:
            self.next_num = None
        return current

    def has_next(self):
        return self.next_num is not None


mat = [[1, 2], [3], [], [4, 5, 6]]

iter_2d = Iterator2D(mat)

assert iter_2d.next() == 1
assert iter_2d.has_next()
assert iter_2d.next() == 2
assert iter_2d.next() == 3
assert iter_2d.has_next()
assert iter_2d.next() == 4
assert iter_2d.next() == 5
assert iter_2d.next() == 6
assert not iter_2d.has_next()
assert iter_2d.next() is None