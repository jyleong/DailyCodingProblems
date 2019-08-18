import unittest

'''Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].'''

def largest_subset(nums):
    if len(nums) <= 1:
        return nums

    def largest_subset_helper(array, num_divider, cur_idx, cur_set):
        if cur_idx == len(array):
            return cur_set

        # take or not take idx
        not_taken = largest_subset_helper(array, num_divider, cur_idx + 1, cur_set)
        num_to_test = array[cur_idx]
        if num_to_test % num_divider == 0:
            # must add
            taken = largest_subset_helper(array, num_to_test, cur_idx + 1, cur_set + [num_to_test])
            return taken if len(taken) > len(not_taken) else not_taken
        return not_taken
    result = largest_subset_helper(nums, 1, 0, [])

    return result


class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = [3, 5, 10, 20, 21]
        result = [5, 10, 20]
        self.assertEqual(largest_subset(test), result)

    def test_case_2(self):
        test = [1, 3, 6, 24]
        result = [1, 3, 6, 24]
        self.assertEqual(largest_subset(test), result)

    def test_case_3(self):
        test = [5]
        result = [5]
        self.assertEqual(largest_subset(test), result)

    def test_case_4(self):
        test = [3, 5]
        result = [5]
        self.assertEqual(largest_subset(test), result)


if __name__ == '__main__':
    unittest.main()


