'''
Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.



'''

def min_diff(arr):
    if not arr or len(arr) == 0:
        return (set(), set())
    sum_1 = 0
    for item in arr:
        sum_1 += item
    result = (None, None)
    def min_diff_helper(s_1, s_2, set_sum_1, set_sum_2):
        cur_diff = abs(set_sum_1 - set_sum_2)
        result = None
        for i in range(len(s_1)):
            elem = s_1[i]
            sum_1 = set_sum_1 - elem
            sum_2 = set_sum_2 + elem
            new_diff = abs(sum_1 - sum_2)
            if new_diff < cur_diff:
                cur_diff = new_diff
                result = (s_1[:i] + s_1[i+1:], s_2 + [elem], sum_1, sum_2)
        if not result:
            return (set(s_1), set(s_2))
        return min_diff_helper(result[0], result[1], sum_1, sum_2)
    arr_copy = arr.copy()
    return min_diff_helper(arr_copy, [], sum_1, 0)


res_1 = [10, 25]
res_2 = [5, 15, 20]
test = [5, 10, 15, 20, 25]
assert min_diff(test) == (set(res_1), set(res_2)) or \
        min_diff(test) == (set(res_2), set(res_1))

res_1_1 = [10, 15]
res_2_1 = [5, 20]
test_2 = [5, 10, 15, 20]
assert min_diff(test_2) == (set(res_1_1), set(res_2_1)) or \
        min_diff(test_2) == (set(res_2_1, set(res_1_1)))
