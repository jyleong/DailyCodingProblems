'''
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
'''

def can_shift(A, B):
    if (not A or not B or (len(A) != len(B))):
        return False

    for idx in range(len(B)):
        left_B = B[0:idx]
        right_B = B[idx:]
        if (right_B + left_B == A):
            return True
    return False


assert not can_shift("", "google")
assert can_shift("abcde", "cdeab")
assert not can_shift("abc", "acb")

assert can_shift("amazon", "azonam")
assert can_shift("amazon", "onamaz")

assert not can_shift("abc", "treeag")