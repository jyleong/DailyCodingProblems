'''
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
'''
import unittest

class SparseArray(object):

    def __init__(self, arr):
        self.dict = dict()
        for i in range(len(arr)):
            if arr[i] != 0:
                self.dict[i] = arr[i]

    def set(self, i, val):
        if val == 0:
            del self.dict[i]
            return
        self.dict[i] = val
        

    def get(self, i):
        if i not in self.dict.keys():
            return 0
        return self.dict[i]

class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        arr = [0, 4 ,0, 5, 3, 0, 0, 9, 10]
        sparse = SparseArray(arr)
        
        self.assertEqual(sparse.get(1), 4)
        self.assertEqual(sparse.get(0), 0)
        sparse.set(0, 13)
        self.assertEqual(sparse.get(0), 13)
        sparse.set(3, 0)
        self.assertEqual(sparse.get(3), 0)
        


if __name__ == '__main__':

    unittest.main()
        

