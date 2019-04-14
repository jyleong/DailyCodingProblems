import unittest
import math
'''
We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three 
inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: 
every distinct pair forms an inversion.

'''


def count_inversions(arr):
    temp = [0] * len(arr)
    return mergeSort(arr, temp, 0, len(arr)-1);

def mergeSort(arr, temp, l, r):
    inv_count = 0
    if r > l: 
        mid = math.floor((r + l) / 2); 

        inv_count = mergeSort(arr, temp, l, mid)
        inv_count += mergeSort(arr, temp, mid + 1, r)
  
        inv_count += merge(arr, temp, l, mid + 1, r)
    
    return inv_count

def merge(arr, temp, l, mid, r):
    i = l
    j = mid
    k = l
    inv_count = 0
    while(i <= mid-1 and j <= r):
        if (arr[i] > arr[j]):
            temp[k] = arr[j]
            inv_count += mid - i
            k += 1
            j += 1
        else:
            temp[k] = arr[i]
            k += 1
            i += 1

    while (i <= mid - 1):
        temp[k] = arr[i]
        k += 1
        i += 1 
  
    while (j <= r):
        temp[k] = arr[j]
        k += 1
        j += 1 
  
    i = l
    while(i <= r):
        arr[i] = temp[i]
        i += 1
  
    return inv_count; 

def countInversions(arr):
    inv_count = 0
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        countInversions(L) # Sorting the first half 
        countInversions(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
                inv_count += mid - i
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return inv_count


class Count_Inversions_Test(unittest.TestCase):
    def test_case_1(self):
        test_case = [1,2,3,4,5]
        result = 0
        
        self.assertEqual(countInversions(test_case), result)

    def test_case_2(self):

        test_case = [2, 4, 1, 3, 5]
        result = 3
        self.assertEqual(countInversions(test_case), result)

    def test_case_3(self):

        test_case = [5,4,3,2,1]
        result = 10
        self.assertEqual(countInversions(test_case), result)


if __name__ == '__main__':

    unittest.main()