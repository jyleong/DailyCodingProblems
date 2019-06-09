'''
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], 
one partition may be [9, 3, 5, 10, 10, 12, 14].
'''
import unittest

def swap(arr, l, r):
    temp = arr[r]
    arr[r] = arr[l]
    arr[l] = temp
    return

def three_partitions(arr, x):
    if (arr is None or len(arr) == 0):
        return []
    l = 0
    i = 0
    h = len(arr) - 1
    while i <= h:
        if (arr[i] < x):
            swap(arr, l, i)
            l += 1
            i += 1
        elif (arr[i] > x):
            swap(arr, i, h)
            h -= 1
        else:
            i += 1

    return arr


class DailyCodingProblemsTest(unittest.TestCase):

    def test_case_1(self):
        test_case = [9, 12, 3, 5, 14, 10, 10]
        target = 10
        result = [9, 3, 5, 10, 10, 14, 12]
        
        self.assertEqual(three_partitions(test_case, target), result)

    def test_case_2(self):

        test_case = []
        target = 8
        result = []
        self.assertEqual(three_partitions(test_case, target), result)

    def test_case_3(self):

        test_case = [6, 9, 10, 3, 17, 4, 4, 2, 9, 12, 13]
        target = 12
        result = [6, 9, 10, 3, 4, 4, 2, 9, 12, 13, 17]
        self.assertEqual(three_partitions(test_case, target), result)

    def test_case_4(self):

        test_case = None
        target = 12
        result = []
        self.assertEqual(three_partitions(test_case, target), result)



if __name__ == '__main__':
    unittest.main()