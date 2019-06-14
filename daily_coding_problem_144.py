'''
Given an array of numbers and an index i, return the index of the nearest 
larger number of the number at index i, 
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. 
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
'''
import unittest
def nearest_larger(arr, idx):

    if idx < 0 or idx > len(arr)-1:
        return

    dist = 0
    while(idx - dist >= 0 or idx + dist <= len(arr)-1):
        min_left = None
        min_right = None
            # left num
        if idx-dist >= 0 and arr[idx - dist] > arr[idx]:
            min_left = arr[idx-dist]

        # right num
        if idx + dist <= len(arr)- 1 and arr[idx + dist] > arr[idx]:
            min_right = arr[idx+dist]

        if min_left is not None and min_right is not None:
            # get min of them
            if min_left < min_right:
                return idx - dist
            else:
                return idx + dist
        if min_left is not None:
            return idx - dist
        if min_right is not None:
            return idx + dist
        dist += 1
    return

class DailyCodingProblemsTest(unittest.TestCase):

    def test_case_1(self):
        test_case = [4, 1, 3, 5, 6]
        target = 0
        result = 3
        
        self.assertEqual(nearest_larger(test_case, target), result)

    def test_case_2(self):

        test_case = [2, 3, 5]
        target = 8
        result = None
        self.assertEqual(nearest_larger(test_case, target), result)

    def test_case_3(self):

        test_case = [11, 8, 6, 9, 10, 9, 12, 1]
        target = 3
        result = 4
        self.assertEqual(nearest_larger(test_case, target), result)

    def test_case_4(self):

        test_case = [11, 8, 15, 9, 10, 9, 12, 17]
        target = 6
        result = 7
        self.assertEqual(nearest_larger(test_case, target), result)

    def test_case_5(self):

        test_case = [11, 8, 15, 9, 10, 5, 4, 5]
        target = 6
        result = 7
        self.assertEqual(nearest_larger(test_case, target), result)


if __name__ == '__main__':
    unittest.main()