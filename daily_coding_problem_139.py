'''
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().
'''

class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_val = next(self.iterator)

    def peek(self):
        return self.next_val
        
    def next(self):
        result = self.next_val
        try:
            self.next_val = next(self.iterator)
        except:
            self.next_val = None

        return result

    def hasNext(self):
        if (self.next_val is not None):
            return True
        return False

# Tests

sample_list = [1, 2, 3, 4, 5]
iterator = iter(sample_list)
peekable = PeekableInterface(iterator)

assert peekable.peek() == 1
assert peekable.hasNext()

assert peekable.next() == 1
assert peekable.next() == 2
assert peekable.next() == 3

assert peekable.peek() == 4
assert peekable.hasNext()

assert peekable.next() == 4
assert peekable.hasNext()
assert peekable.peek() == 5
assert peekable.next() == 5

assert not peekable.hasNext()
assert not peekable.peek()