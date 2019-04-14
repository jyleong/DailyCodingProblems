'''
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.'''


def powerset(A):
    if A == []:
        return [[]]
    a = A[0]
    incomplete_pset = powerset(A[1:])
    rest = [[a] + set for set in incomplete_pset]
    return rest + incomplete_pset

set_test_1 = [1,2,3]

set_test_2 = []

res_1 = powerset(set_test_1)

res_2 = powerset(set_test_2)

print("test 1: ")
print(res_1)

print("test 2: ")
print(res_2)