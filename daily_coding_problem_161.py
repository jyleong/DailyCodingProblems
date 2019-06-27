'''
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
'''

def reverse(num):
    copy = num
    res = 0
    while copy > 0:
        if copy & 1 == 1:
            res = (res << 1) + 1
        else:
            res = res << 1
        copy = copy >> 1
        
    return res

assert reverse(11) == 13
assert reverse(10) == 5