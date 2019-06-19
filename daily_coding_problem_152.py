'''
You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
'''

from random import uniform

def bin_search(sum_probs, val):
    l = 0
    h = len(sum_probs) - 1
    while l < h:
        mid = l + ((h - l) / 2)
        if val > sum_probs[mid]: 
            l = mid + 1
        else:
            h = mid  
      
    if sum_probs[l] >= val:
        return l
    else:
        return -1  

def gen_with_prob(nums, probs):
    sum_probs = [0] * len(probs)
    sum_probs[0] = probs[0]

    for idx in range(1, len(probs)):
        sum_probs[idx] = sum_probs[idx-1] + probs[idx]

    val = uniform(0,1)
    # binary search through sum_probs
    index = bin_search(sum_probs, val)
    return nums[index]

for i in range(100):
    val = gen_with_prob([1, 2 ,3 ,4], [0.1, 0.5, 0.2, 0.2])
    print("Test {}: result {}".format(i+1, val))