'''
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
'''

class BitArray(object):

    def __init__(self, size):
        self.bit_array = [0]*size
        self.size = size

    def set(self, i, val):
        if i >= self.size:
            raise LookupError("Invalid Index")
        self.bit_array[self.size - i - 1] = val

    def get(self, i):
        if i >= self.size:
            raise LookupError("Invalid Index")
        return int(self.bit_array[self.size - i - 1])

    def str_rep(self):
        return ''.join([str(b) for b in self.bit_array])




bit_arr = BitArray(8)

assert bit_arr.get(0) == 0
bit_arr.set(0, 1) 
assert bit_arr.get(0) == 1
assert bit_arr.str_rep() == '00000001'

bit_arr.set(7, 1)

bit_arr.set(5, 1)
bit_arr.set(0, 0)

assert bit_arr.str_rep() == '10100000' 
try:
    bit_arr.set(10, 1)
except LookupError as le:
    print(le)