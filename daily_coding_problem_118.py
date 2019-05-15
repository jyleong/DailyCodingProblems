'''
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''
import unittest

def square_sort(arr):
    position_positive = 0
    for i in range(len(arr)):
        if (arr[i] > 0):
            position_positive = i
            break
    squared = list(map(lambda x: x**2, arr))
    left = list(reversed(squared[:position_positive]))
    square = merge_sort(left[:position_positive], squared[position_positive:])
    return square

def merge_sort(a_1, a_2):
    res = []

    i = 0;
    j = 0
    while(i < len(a_1) and j < len(a_2)):
        if (a_1[i] < a_2[j]):
            res.append(a_1[i])
            i += 1
        else:
            res.append(a_2[j])
            j += 1
    while(i < len(a_1)):
        res.append(a_1[i])
        i += 1
    while(j < len(a_2)):
        res.append(a_2[j])
        j += 1
    return res


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        case = [-9, -2, 0, 2, 3]
        
        expected = [0, 4, 4, 9, 81]
        self.assertEqual(square_sort(case), expected)

    def test_case_2(self):
        case = [-12, -3, -1, 9, 15, 20]
        
        expected = [1, 9, 81, 144, 225, 400]
        self.assertEqual(square_sort(case), expected)

    def test_case_3(self):
        case = [-4, -2, 0, 1, 8, 12, 13]
        
        expected = [0, 1, 4, 16, 64, 144, 169]
        self.assertEqual(square_sort(case), expected)

    def test_case_4(self):
        case = []
        
        expected = []
        self.assertEqual(square_sort(case), expected)

if __name__ == '__main__':

    unittest.main()

