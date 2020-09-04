'''
Given an array of numbers N and an integer k, your task is to split N into k partitions such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal partition is [5, 1, 2], [7], [3, 4].
'''

def too_large(mid, arr, k):

    num_parts = 0
    total = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            return False
        total += arr[i]
        if total > mid:
            num_parts += 1
            # reset total, represents new partition
            total = arr[i]
    num_parts += 1
    return num_parts <= k

def minimize_partitions(arr, k):
    low = 1
    high = sum(arr)
    while(low <= high):
        mid = low + (high - low)//2
        if (too_large(mid, arr, k)):
            high = mid-1
            answer = mid
        else:
            low = mid + 1
    return answer

assert minimize_partitions([5, 1, 2, 7, 3, 4], k=3) == 8
